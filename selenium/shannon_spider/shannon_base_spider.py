# -*- coding: utf-8 -*-

import re
import logging
import collections
import scrapy
import traceback
import hashlib
from datetime import datetime
from typing import NamedTuple

from urllib.parse import unquote

from scrapy import signals

from shannon_spider.util import get_log_url
from shannon_spider.util.notify import send_dingtalk
from shannon_spider.db import ItemBaseModel, history_item_model, create_table
from shannon_spider.util import request_to_json
from shannon_spider.util.rfc6266 import parse_filename


class ShannonCrawledItem(scrapy.item.DictItem):
    '''
    保存解析结果
    '''
    def __init__(self, spider, response, *args, **kwargs):
        scrapy.item.DictItem.__init__(self, *args, **kwargs)

        if not isinstance(spider, ShannonBaseSpider):
            raise ValueError('spider: {}, must be instance of {}'.format(type(response).__name__, ShannonBaseSpider.__name__))
        
        if not isinstance(response, scrapy.http.Response):
            raise ValueError('response: {}, must be instance of {}'.format(type(response).__name__, scrapy.http.Response.__name__))

        url_sha, req_repr = spider.request_sha(response.request)

	# 下面的k-v对是给history table使用的, 每个返回的item必须包含这几个字段
        self['url_sha'] = url_sha
        self['req_repr'] = req_repr # request 的序列化结果, json格式
        self['expire'] = None # 过期时间(秒), None 或 -1 表示永不过期
        self['last_updated'] = datetime.now() # 最后一次更新时间
        # need_update_id 表示要更新的id，由DupeFilterMiddleware控制, None表示没有过期，不需要更新
        self['need_update_id'] = response.meta.get('need_update_id', None) 
        self['is_end'] = True  # 用来选择是否要产生一个history_item
        # 当前item 要下载的文件的 url
        self['file_urls'] = []
        # 下载成功的文件信息
        self['files'] = []
        # 当前item 要下载的图片的 url
        self['image_urls'] = []
        # 下载成功的图片信息
        self['images'] = []
        self['sha'] = None
    
    def __setitem__(self, key, value):
        self.fields[key] = {}
        self._values[key] = value


class FileUri(NamedTuple):
    '''
    file资源
    url: 资源链接
    name: 文件名, 不包含扩展名
    ext: 资源扩展名, 默认为 None
    '''
    url: str
    name: str = None
    ext: str = None
    folder: str = None


class ImageUri(NamedTuple):
    '''
    image资源
    url: 资源链接
    ext: 资源扩展名, 默认为 None 
    '''
    url: str
    name: str = None
    ext: str = None
    folder: str = None


class ShannonBaseSpider(scrapy.Spider):
    '''
    shannon 爬虫基类, 主要进行一些必要的属性检查, 类型检查等
    '''
    result_orm_model = None # 要保存到数据库中的结果的 orm 类
    allow_partial_file_downloaded = False # 当需要下载文件时, 是否允许部分下载成功, 默认不允许, 当有文件下载失败时，这个item不能写入数据库
    auto_check_insert_count = True  # 是否自动检查插入数据量
    check_insert_count = 0  # 默认插入数量最小值
    must_have_new_data = False  # 考虑去重因素后, 必须有新数据插入

    def __init__(self, result_orm_model=None, name=None, **kwargs):
        scrapy.Spider.__init__(self, name, **kwargs)
        if result_orm_model is not None:
            self.result_orm_model = result_orm_model
        elif not getattr(self, 'result_orm_model', None):
            raise ValueError("%s must have a result_orm_model" % type(self).__name__)
        elif not issubclass(self.result_orm_model, ItemBaseModel):
            raise ValueError("result_orm_model must be subclass of %s" % ItemBaseModel.__name__)
        # 创建 result table 和 history table
        create_table(self.result_orm_model)
        if self.result_orm_model not in history_item_model:
            raise ValueError('create history table failed.')
        self.error_list = list()
        # 确定某些字段不用于生成哈希值去重
        self.not_set_sha = set()

    def set_sha(self, item: ShannonCrawledItem):
        '''
        接受要在mysql中查重的item,生成一个sha值,供日后查重用
        '''
        self_attributes = ['id', 'url_sha', 'req_repr', 'expire', 'last_updated', 'need_update_id',
                           'is_end', 'file_urls', 'files', 'image_urls', 'images', 'sha']
        hash_code = hashlib.sha1()
        hash_string = ''
        for key, value in item.items():
            if key not in self_attributes and key not in self.not_set_sha:
                if value is None:
                    hash_string += ''
                else:
                    hash_string += str(value)
        hash_code.update(hash_string.encode('utf-8'))
        sha = hash_code.hexdigest()
        return sha
 
    def build_orm_item(self, item: ShannonCrawledItem) -> ItemBaseModel:
        '''
        将dict类型的item转成orm item, 如果item不符合规范，直接返回None即可将此 item 抛弃
        '''
        if not isinstance(item, ShannonCrawledItem):
            raise ValueError('item: {}, must be instance of {}'.format(type(item).__name__, ShannonCrawledItem.__name__))
        
        orm_item = self.result_orm_model()
        columns = item.fields
        for column in columns:
            setattr(orm_item, column, item[column])
            
        return orm_item

    def request_sha(self, request: scrapy.Request) -> (int, str):
        '''
        计算一个请求的指纹, 用于去重, 返回值是一个 <int, json_str>
        int 主要用于索引, 方便快速检索. json_str 是 request 的 json 序列化结果
        '''
        if not isinstance(request, scrapy.Request):
            raise ValueError('request: %s, must be instance of %s' % (type(request).__name__, scrapy.Request.__name__))
        hash = hashlib.sha1()
        hash.update(str(request_to_json(request)).encode('utf-8'))
        url_sha = hash.hexdigest()
        return url_sha, request_to_json(request)

    def parse_origin_filename(self, request = None, response = None , ext=None):
        '''
        从response中解析文件名称
        '''
        if request and not isinstance(request, scrapy.http.Request):
            raise ValueError('request: %s, must be instance of %s' % (type(request).__name__, scrapy.http.Request.__name__))

        if response and not isinstance(response, scrapy.http.Response):
            raise ValueError('response: %s, must be instance of %s' % (type(response).__name__, scrapy.http.Response.__name__))

        try:
            if 'Content-Disposition' in response.headers:
                header = response.headers['Content-Disposition'].decode('ascii')
                return parse_filename(header, relaxed=True).filename_sanitized(ext)
        except Exception as e:
            self.logger.warning('exception: {}'.format(e))
            self.logger.warning(traceback.format_exc())

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(ShannonBaseSpider, cls).from_crawler(crawler, *args, **kwargs)
        # crawler.signals.connect(spider.spider_error, signal=signals.spider_error)
        return spider

    # def spider_error(self, failure, response, spider):
    #
    #     try:
    #         error = failure.frames
    #     except:
    #         error = failure
    #     try:
    #         log_url = get_log_url(spider.name)
    #         send_dingtalk('spider_error', spider.name, str(error), log_url)
    #     except BaseException as e:
    #         self.logger.error('spider_error钉钉报警发送失败{}'.format(e))

    @staticmethod
    def close(spider, reason):
        scrapy.Spider.close(spider, reason)
        if spider.auto_check_insert_count:
            insert_count = spider.crawler.stats.get_value('insert_count', 0)
            send_error = False
            if insert_count <= spider.check_insert_count:
                if spider.must_have_new_data:
                    send_error = True
                else:
                    duplicated_count = spider.crawler.stats.get_value('duplicated_count', 0)
                    if duplicated_count == 0:
                        send_error = True
            if send_error:
                try:
                    error = f'爬虫: {spider.name}, 插入数量异常, 插入: {insert_count}条, 小于最低值: {spider.check_insert_count}, 请及时查看原因!!!'
                    log_url = get_log_url(spider.name)
                    send_dingtalk('spider_error', spider.name, str(error), log_url)
                except BaseException as e:
                    spider.logger.error('spider_error钉钉报警发送失败{}'.format(e))
