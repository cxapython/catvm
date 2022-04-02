# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime
import hashlib
import traceback
from urllib.parse import urljoin, urlparse
from io import BytesIO
from twisted.internet import defer
from copy import deepcopy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy import PrimaryKeyConstraint, ForeignKey
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, create_engine
from sqlalchemy.types import VARCHAR, Integer, String, TEXT, Date, DateTime

import boto3
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline, FSFilesStore, FileException
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes

from shannon_spider.db import Session, history_item_model
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

from shannon_spider.shannon_base_spider import ShannonBaseSpider, ShannonCrawledItem
from shannon_spider.shannon_base_spider import FileUri, ImageUri 

from shannon_spider.util import sha1sum, md5sum


class ShannonFSFileStore(FSFilesStore):
    '''
    本地存储
    '''
    def __init__(self, basedir):
        FSFilesStore.__init__(self, basedir)

    def stat_file(self, path, info):
        absolute_path = self._get_filesystem_path(path)
        try:
            last_modified = os.path.getmtime(absolute_path)
        except os.error:
            info.spider.logger.debug('getmtime error, path: {}'.format(path))
            return {}

        with open(absolute_path, 'rb') as f:
            checksum = md5sum(f)

        return {'last_modified': last_modified, 'checksum': checksum}


class ShannonOSSFileStore(object):
    '''
    用aliyun oss作为后端存储
    '''
    OSS_ACCESS_KEY_ID = None
    OSS_ACCESS_KEY_SECRET = None
    OSS_ENDPOINT = None
    OSS_CONNECT_TIMEOUT = None
    
    def __init__(self, uri):
        import oss2
        assert uri.startswith('oss://')
        self.OSS_BUCKET_NAME, self.prefix = uri[6:].split('/', 1)
        self.bucket = oss2.Bucket(oss2.Auth(self.OSS_ACCESS_KEY_ID, self.OSS_ACCESS_KEY_SECRET),
                self.OSS_ENDPOINT,
                self.OSS_BUCKET_NAME,
                connect_timeout=self.OSS_CONNECT_TIMEOUT)

    def stat_file(self, path, info):
        key_name = os.path.join(self.prefix, path)
        try:
            head = self.bucket.head_object(key_name)
            last_modified = head.last_modified
            checksum = head.etag.strip('"')
            info.spider.logger.debug('oss stat_file: path: {}, last_modified: {}, checksum: {}'.format(key_name, datetime.fromtimestamp(last_modified), checksum))
        except oss2.exceptions.NotFound as e:
            info.spider.logger.debug('oss file {} not found'.format(key_name))
            return {}

        return {'last_modified': last_modified, 'checksum': checksum}

    def persist_file(self, path, buf, info, meta=None, headers=None):
        """
        upload file to oss storage
        """
        key_name = os.path.join(self.prefix, path)
        buf.seek(0)
        i = 0
        while i < 3:
            try:
                result = self.bucket.put_object(key_name, buf)
                if result.status == 200:
                    break
                else:
                    i += 1
            except:
                i += 1


class ShannonS3FileStore(object):
    '''
    用aws S3作为后端存储
    '''
    S3_BUCKET = None
    S3_REGION = None
    S3_ACCESS_KEY = None
    S3_SECRET_KEY = None

    def __init__(self, uri):
        assert uri.startswith('s3://')
        self.prefix, self.s3_bucket_name = uri[5:].split('/', 1)
        self.bucket = boto3.client('s3', region_name=self.S3_REGION, aws_access_key_id=self.S3_ACCESS_KEY, aws_secret_access_key=self.S3_SECRET_KEY)

    def stat_file(self, path, info):
        '''判断文件是否存在'''
        key_name = os.path.join(self.prefix, path).replace('{}\\'.format(self.prefix), '{}/'.format(self.prefix))  # windows中\的问题
        try:
            head = self.bucket.head_object(Bucket=self.S3_BUCKET, Key=key_name)
            last_modified = head['LastModified']
            checksum = head['ETag'].strip('"')
            info.spider.logger.debug('s3 stat_file: path: {}, last_modified: {}, checksum: {}'.format(key_name, last_modified, checksum))
        except boto3.exceptions.ResourceNotExistsError as e:
            info.spider.logger.debug('s3 file {} not found'.format(key_name))
            return {}
        last_modified = int(time.mktime(time.strptime(str(last_modified).split('+')[0], "%Y-%m-%d %H:%M:%S")))
        return {'last_modified': last_modified, 'checksum': checksum}

    def persist_file(self, path, buf, info, headers=None):  # meta=None,
        """
        upload file to s3 storage
        """
        key_name = os.path.join(self.prefix, path).replace('{}\\'.format(self.prefix), '{}/'.format(self.prefix))  # windows中\的问题
        i = 0
        while i < 3:
            try:
                result = self.bucket.put_object(Body=buf, Bucket=self.S3_BUCKET, Key=key_name)
                if result['ResponseMetadata']['HTTPStatusCode'] == 200:
                    break
                else:
                    i += 1
            except Exception as e:
                i += 1
                if i == 3:
                    info.spider.logger.warning('upload file {} fail, error:{}'.format(key_name, e))


class ShannonFilesPipeline(FilesPipeline):
    '''
    下载文件, 需要下载的文件链接保存在 item['file_urls']: list(FileUri) 中,
    此pipeline会自动处理下载, 去重, 保存等工作, 并将文件路径放到 item['files'] 中
    '''

    def __init__(self, store_uri, download_func=None, settings=None):
        FilesPipeline.__init__(self, store_uri, download_func, settings)
        self.store_uri = store_uri
        if settings and settings['FILES_EXPIRES'] is None or settings['FILES_EXPIRES'] < 0:
            self.expires = 3650000 # files expires after 10000 years

    @classmethod
    def from_settings(cls, settings):
        cls.STORE_SCHEMES['file'] = ShannonFSFileStore
        cls.STORE_SCHEMES['oss'] = ShannonOSSFileStore
        cls.STORE_SCHEMES['s3'] = ShannonS3FileStore

        oss_store = cls.STORE_SCHEMES['oss']
        oss_store.OSS_ACCESS_KEY_ID = settings['OSS_ACCESS_KEY_ID']
        oss_store.OSS_ACCESS_KEY_SECRET = settings['OSS_ACCESS_KEY_SECRET']
        oss_store.OSS_ENDPOINT = settings['OSS_ENDPOINT']
        oss_store.OSS_CONNECT_TIMEOUT = settings['OSS_CONNECT_TIMEOUT']

        s3_store = cls.STORE_SCHEMES['s3']
        s3_store.S3_BUCKET = settings['S3_BUCKET']
        s3_store.S3_REGION = settings['S3_REGION']
        s3_store.S3_ACCESS_KEY = settings['S3_ACCESS_KEY']
        s3_store.S3_SECRET_KEY = settings['S3_SECRET_KEY']

        store_uri = settings['FILES_STORE']
        return cls(store_uri, settings=settings)

    def get_media_requests(self, item, info):
        for file_uri in item.get('file_urls', []):
            if not isinstance(file_uri, FileUri):
                raise ValueError('file_url: %s must be type of %s' % (type(file_uri).__name__, FileUri.__name__))

            request = scrapy.Request(file_uri.url)
            request.meta['type'] = 'file'
            request.meta['name'] = file_uri.name # 用户指定的文件名
            request.meta['ext'] = file_uri.ext # 文件扩展名
            request.meta['folder'] = file_uri.folder
            yield request

    def file_path(self, request, response=None, info=None):
        # 首先获取用户设置的扩展名, 如果没有找到, 就从url中自动判断扩展名 (所以扩展名可能为空)
        ext = request.meta.get('ext', None)
        if not ext:
            url = urljoin(request.url, urlparse(request.url).path)
            ext = os.path.splitext(url)[1]
        if ext and not ext.startswith('.'):
            ext = '.' + ext

        # 如果用户没有设置文件名, 就用 request 的sha1 作为文件名 
        filename = request.meta.get('name', None)
        if filename is None:
            url_sha, req_repr = info.spider.request_sha(request)
            file_guid = hashlib.sha1(to_bytes(req_repr)).hexdigest()
            filename = file_guid
        filename = '%s%s' % (filename, ext)
        folder = request.meta.get('folder', None)
        if folder:
            path = '%s/%s' % (folder, filename)
        else:
            path = '%s/%s' % (info.spider.name, filename)
        info.spider.logger.debug('file path: %s' % path)
        return path

    def item_completed(self, results, item, info):
        if isinstance(item, ShannonCrawledItem):
            item['files'] = []
            for ok, res in results:
                if not ok:
                    continue
                res = deepcopy(res)
                res['path'] = os.path.join(self.store_uri, res['path'])
                item['files'].append(res)
        return item

    def media_downloaded(self, response, request, info):
        if response.status == 5003:
            raise FileException('download-error')
        elif response.status != 200:
            info.spider.logger.error('File (code: {}): Error downloading file from {}'.format(response.status, request))
            raise FileException('download-error')
        return FilesPipeline.media_downloaded(self, response, request, info)


class ShannonImagesPipeline(ImagesPipeline):
    '''
    下载图片, 图片也是文件, 之所以分开, 是为了对图片进行一些特殊处理, 如格式转换等
    '''
    def __init__(self, store_uri, download_func=None, settings=None):
        ImagesPipeline.__init__(self, store_uri, download_func, settings)
        self.store_uri = store_uri
        if settings and settings['IMAGES_EXPIRES'] is None or settings['IMAGES_EXPIRES'] < 0:
            self.expires = 3650000 # images expires after 10000 years

    @classmethod
    def from_settings(cls, settings):
        cls.STORE_SCHEMES['file'] = ShannonFSFileStore
        cls.STORE_SCHEMES['oss'] = ShannonOSSFileStore

        oss_store = cls.STORE_SCHEMES['oss']
        oss_store.OSS_ACCESS_KEY_ID = settings['OSS_ACCESS_KEY_ID']
        oss_store.OSS_ACCESS_KEY_SECRET = settings['OSS_ACCESS_KEY_SECRET']
        oss_store.OSS_ENDPOINT = settings['OSS_ENDPOINT']

        store_uri = settings['IMAGES_STORE']
        return cls(store_uri, settings=settings)

    def get_media_requests(self, item, info):
        for image_uri in item.get(self.images_urls_field, []):
            if not isinstance(image_uri, ImageUri):
                raise ValueError('image_url: %s must be type of %s' % (type(image_uri).__name__, ImageUri.__name__))
            request = scrapy.Request(image_uri.url)
            request.meta['type'] = 'image'
            request.meta['name'] = image_uri.name # 用户指定的图片文件名
            request.meta['ext'] = image_uri.ext # 图片扩展名
            yield request

    def file_path(self, request, response=None, info=None):
        '''
        计算图片的存储路径, 与文件不同, 图片的格式可以从二进制流中推断出来,
        所以无论原始格式是什么, 都可以存储为 jpg, 所以不需要解析文件格式
        '''
        # 首先获取用户设置的扩展名, 如果没有找到, 就用 jpg 格式
        ext = request.meta.get('ext', None)
        if ext and not ext.startswith('.'):
            ext = '.' + ext
        if not ext:
            ext = '.jpg'

        # 如果用户没有设置图片文件名, 就用 request 的sha1 作为文件名 
        imagename = request.meta.get('name', None)
        if imagename is None:
            url_sha, req_repr = info.spider.request_sha(request)
            image_guid = hashlib.sha1(to_bytes(req_repr)).hexdigest()
            imagename = image_guid
        imagename = '%s%s' % (imagename, ext)

        path = '%s/%s' % (info.spider.name, imagename)
        info.spider.logger.debug('image path: %s' % path)
        return path

    def item_completed(self, results, item, info):
        if isinstance(item, ShannonCrawledItem):
            item['images'] = []
            for ok, res in results:
                if not ok:
                    continue
                res = deepcopy(res)
                res['path'] = os.path.join(self.store_uri, res['path'])
                item['images'].append(res)
        return item


class DBPipeline(object):
    '''
    将抓取内容保存到数据库
    '''
    duplicated_count = 0
    insert_count = 0
    def open_spider(self, spider):
        if not issubclass(spider.__class__, ShannonBaseSpider):
            raise ValueError('spider: %s must be subclass of %s' %(type(spider).__name__, ShannonBaseSpider.__name__))

    def process_item(self, item, spider):
        # validation verify
        if not isinstance(item, ShannonCrawledItem):
            spider.logger.error('item: {} must be type of {}'.format(type(item).__name__, ShannonCrawledItem.__name__))
            raise DropItem('item: {} must be type of {}'.format(type(item).__name__, ShannonCrawledItem.__name__))

        if len(item.get("file_urls", [])) != 0:
            if not item.get("files", []):
                raise DropItem('pdf下载失败')

        # save result item and history item in one transaction
        orm_item = None
        history_item = None
        session = Session()
        try:
            orm_item = spider.build_orm_item(item)
            orm_item.sha = spider.set_sha(item)
            orm_item.url_sha = item['url_sha']
            if orm_item is None:
                spider.logger.debug('item: {}'.format(item))
                raise DropItem('user drop item')

            if not issubclass(orm_item.__class__, CommonFieldMixin):
                raise DropItem('item: {} must mixin {}'.format(orm_item.__class__.__name__, CommonFieldMixin.__name__))

            if not issubclass(orm_item.__class__, ItemBaseModel):
                raise DropItem('item: {} must be subclass of {}'.format(orm_item.__class__.__name__, ItemBaseModel.__name__))

            if item['need_update_id'] is not None:
                spider.logger.debug('need_update_id: {}'.format(item['need_update_id']))
                old_orm_item = session.query(orm_item.__class__).filter(orm_item.__class__.id == item['need_update_id']).first()
                for k, v in vars(orm_item).items():
                    # 如果不是None才更新，防止不可预期的更新
                    if not k.startswith('_') and v is not None and getattr(old_orm_item, k) != v:
                        setattr(old_orm_item, k, v)
                orm_item = old_orm_item

            if orm_item.sha is not None:
                query = session.query(spider.result_orm_model).filter(spider.result_orm_model.sha == orm_item.sha)
                dup = query.first()
                if dup:
                    self.duplicated_count += 1
                    spider.logger.debug("抓取到了重复数据,已跳过 过滤哈希值为{}".format(orm_item.sha))
                    if item['is_end']:
                        try:
                            HistoryModel = history_item_model[orm_item.__class__]
                            history_item = HistoryModel()
                            history_item.url_sha = item['url_sha']
                            history_item.req_repr = item['req_repr']
                            history_item.last_updated = item['last_updated']
                            query = session.query(HistoryModel).filter(and_(HistoryModel.url_sha == history_item.url_sha, HistoryModel.req_repr == history_item.req_repr))
                            history = query.first()
                            if not history:
                                spider.logger.debug('数据重复,但历史记录不存在,该数据为旧数据库迁移数据')
                                session.add(history_item)
                                session.commit()
                                spider.logger.debug('已补充历史记录')
                            else:
                                spider.logger.debug('数据和历史记录都重复 不对数据库进行任何写入操作')
                        except Exception:
                            traceback.print_exc()
                    else:
                        spider.logger.debug('该条数据设定不添加历史记录')
                    session.close()
                    return
            session.add(orm_item)
            session.flush()
            if item['is_end'] == True:
                HistoryModel = history_item_model[orm_item.__class__]
                history_item = HistoryModel()
                history_item.url_sha = item['url_sha']
                history_item.req_repr = item['req_repr']
                history_item.last_updated = item['last_updated']
                if item['expire'] is not None and item['expire'] >= 0:
                    history_item.expire = item['expire']

                if item['need_update_id'] is not None:
                    old_history_item = session.query(HistoryModel).filter(and_(HistoryModel.type == 0, HistoryModel.ref_id == item['need_update_id'])).first()
                    for k, v in vars(history_item).items():
                        # 如果不是None才更新，防止不可预期的更新
                        if not k.startswith('_') and v is not None and getattr(old_history_item, k) != v:
                            setattr(old_history_item, k, v)
                    history_item = old_history_item

                session.add(history_item)
            self.insert_count += 1
            session.commit()

            if item['need_update_id'] is not None:
                spider.crawler.stats.inc_value('updated_count')
        except Exception as e:
            session.rollback()
            spider.logger.warning('save item failed, have rollback. result_item: [%s], history_item[%s], exception: %s' % (orm_item, history_item, e))
            raise DropItem('save item failed, have rollback. exception: %s' % e)
        finally:
            session.close()

    def close_spider(self, spider):
        from shannon_spider.util.notify import send_dingtalk_info
        from shannon_spider.util import get_service_url, get_service_url_aws, get_log_url
        spider.crawler.stats.set_value('duplicated_count', self.duplicated_count)
        spider.crawler.stats.set_value('insert_count', self.insert_count)
        error_count = spider.crawler.stats.get_value('log_count/ERROR')
        if error_count and error_count > 0:
            # 用于aws机器获取服务地址
            log_url = get_log_url(spider.name)
            # notify_url = os.path.join(get_service_url_aws('notify'), 'dingtalk')
            send_dingtalk_info(spider.name, error_count, log_url)

