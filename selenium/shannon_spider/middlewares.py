# -*- coding: utf-8 -*-
# import asyncio
import asyncio
import base64
import logging
import random
import time
from datetime import datetime, timedelta

import pyppeteer
import requests
import scrapy
from scrapy.http import HtmlResponse
from twisted.internet.defer import Deferred
from twisted.internet.error import ConnectionRefusedError
from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.exceptions import IgnoreRequest

from sqlalchemy.sql import exists
from sqlalchemy import and_

from shannon_spider.db import history_item_model, Session, query_to_sql
from shannon_spider.settings import RETRY_HTTP_CODES, RETRY_TIMES
from shannon_spider.shannon_base_spider import ShannonBaseSpider


class RandomUserAgentMiddleware(object):
    '''
    随机选择user-agent的中间件
    '''
    def __init__(self):
        from shannon_spider.conf.user_agent import USER_AGENT_LIST
        self.user_agent_list = USER_AGENT_LIST 
        self.customized_user_agent = None

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls()
        crawler.signals.connect(obj.spider_opened, signal=signals.spider_opened)
        return obj

    def spider_opened(self, spider):
        if not issubclass(spider.__class__, ShannonBaseSpider):
            raise ValueError('spider: %s must be subclass of %s' %(type(spider).__name__, ShannonBaseSpider.__name__))

        # this is user customized user_agent, assign it in Spider.__init__
        self.customized_user_agent = getattr(spider, 'user_agent', self.customized_user_agent)

    def process_request(self, request, spider):
        if self.customized_user_agent:
            request.headers[b'User-Agent'] = self.customized_user_agent
        else: 
            request.headers[b'User-Agent'] = random.choice(self.user_agent_list)
        # print("request.headers:", request.headers)


class SelectHttpProxyMiddleware(object):
    '''
    随机选择proxy的中间件
    '''
    def __init__(self):
        from shannon_spider.conf.proxy import PROXY_LIST, CONTINUOUS_USE_COUNT
        self.continuous_use_count = CONTINUOUS_USE_COUNT
        self.proxy_list = PROXY_LIST
        self.used_count = {}
        self.failed_count = {}
        self.logger = logging.getLogger('proxy')
        for proxy in self.proxy_list:
            self.used_count[proxy] = 0
            self.failed_count[proxy] = 0

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        obj = cls()
        return obj

    def spider_opened(self, spider):
        if not issubclass(spider.__class__, ShannonBaseSpider):
            raise ValueError('spider: %s must be subclass of %s' %(type(spider).__name__, ShannonBaseSpider.__name__))

    def process_request(self, request, spider):
        if 'proxy' in request.meta:
            return
        
        if len(self.proxy_list) == 0:
            raise KeyError('no valid proxy found, cannot proceed')

        proxy = request.meta['proxy'] if 'proxy' in request.meta else None
        if proxy is None or self.used_count[proxy] == self.continuous_use_count:
            proxy = random.choice(self.proxy_list)
            self.logger.debug("selected proxy: {}".format(proxy))
        if proxy != 'local_direct_connect':
            request.meta['proxy'] = proxy
        else:
            request.meta['proxy'] = None
        self.used_count[proxy] += 1

    def process_exception(self, request, exception, spider):
        if 'proxy' not in request.meta:
            return
        proxy = request.meta['proxy']
        if proxy in self.proxy_list:
            if isinstance(exception, ConnectionRefusedError):
                self.failed_count[proxy] += 1
            self.proxy_list.remove(proxy)
            self.logger.info('Removing failed proxy <%s>, %d proxy left' % (proxy, len(self.proxy_list)))


class DBDupeFilterMiddleware(object):
    '''
    过滤重复请求的中间件
    '''
    def __init__(self):
        self.logger = logging.getLogger('filter')

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls()
        return obj

    def spider_opened(self, spider):
        if not issubclass(spider.__class__, ShannonBaseSpider):
            raise ValueError('spider: %s must be subclass of %s' %(type(spider).__name__, ShannonBaseSpider.__name__))

    def process_request(self, request, spider):
        if request is None or spider is None:
            return
        # 不启用过滤器的请求(如列表页, 导航页等)
        if not request.meta.get('use_dup_filter', False):
            return

        HistoryItemModel = history_item_model[spider.result_orm_model]
        url_sha, req_repr = spider.request_sha(request)
        filtered = False
        try:
            session = Session()
            query = session.query(HistoryItemModel).filter(and_(HistoryItemModel.url_sha == url_sha, HistoryItemModel.req_repr == req_repr))
            if spider.crawler.settings['ECHO_SQL']:
                self.logger.debug(query_to_sql(query))
            history = query.first()
            if history:
                if history.expire >= 0 and history.last_updated + timedelta(seconds=history.expire) <= datetime.now(): 
                    request.meta['need_update_id'] = history.result_id 
                    spider.crawler.stats.inc_value('need_update_count')
                    self.logger.debug('need update {}. last_updated: {}, expire: {}'.format(history.result_id, history.last_updated, history.expire))
                else:
                    filtered = True
                    spider.crawler.stats.inc_value('filtered_count')
                    self.logger.debug('request:[{} : {}] is filtered.'.format(url_sha, req_repr))
            session.commit()
        except Exception as e:
            session.rollback()
            self.logger.warning('exception happened when processing request [{} : {}], exception: {}'.format(url_sha, req_repr, e))
        finally:
            session.close()

        if filtered:
            raise IgnoreRequest()

    def process_response(self, request, response, spider):
        if response.body == b'Frequent operation, please try again in 5 minutes!' or not response.body:
            time.sleep(random.randint(300, 350))
            return request
        else:
            return response

class AbuyunProxyMiddleware(object):
    '''阿布云代理池'''
    # 代理服务器
    proxyServer = "http://http-pro.abuyun.com:9010"

    # 代理隧道验证信息
    proxyUser = 'H5686N8652T8UK8P'
    proxyPass = '02F2327FEFDD0428'
    proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

    def process_request(self, request, spider):
        request.meta["proxy"] = self.proxyServer
        request.headers["Proxy-Authorization"] = self.proxyAuth


    def process_response(self, request, response, spider):
        if response.status == 503 and response.url != 'https://xueqiu.com':
            raise IgnoreRequest()
        else:
            return response

class PdfCheckRetry:
    '''用于pdf检测是否完全下载'''

    def process_response(self, request, response, spider):
        # 判断是否为pdf文件下载
        # 如果返回状态码为5003, 则重试下载后数据依旧不全
        if request.meta.get('ext', "") in ["pdf", "PDF"] and response.status == 200:
            # 判断是否以此结尾
            clean_res = response.body.strip(b'\x00')
            if b"%%EO" not in clean_res[-16:] and b'%%E' not in clean_res[-16:]:
                # 判断是否重试超出阈值
                if request.meta.get("retry_file_down_", 0) > 1:
                    end = clean_res[-16:]
                    spider.logger.error(f"pdf中间件--pdf文件不以%%EO或%%E%结尾：{response.url}, end:{end}")
                    response.status = 5003
                    return response
                request.meta["retry_file_down_"] = request.meta.get("retry_file_down_", 0) + 1
                return request
            else:
                return response
        else:
            return response


def as_deferred(f):
    """Transform a Twisted Deffered to an Asyncio Future"""
    return Deferred.fromFuture(asyncio.ensure_future(f))

import aiohttp

aiohttp_session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
logger = logging.getLogger(__name__)
# hook  禁用 防止监测webdriver
from pyppeteer import launcher
launcher.AUTOMATION_ARGS.remove("--enable-automation")


class PuppeteerMiddleware:
    """Downloader middleware handling the requests with Puppeteer"""

    def __init__(self):
        pyppeteer.DEBUG = False
        self.cookie_dict = {}

    @staticmethod
    async def deal_error(err):
        '''抛弃掉错误'''
        await err.abort()

    async def _process_request(self, request, spider, is_proxy=True):
        """Handle the request using Puppeteer"""
        status = 5003
        content = None
        request_count = 0
        is_wait = False
        cookies = {}

        try:
            self.browser_no_proxy = await pyppeteer.launch(
                logLevel=logging.ERROR, autoClose=False, dumpio=True, headless=False,
            )
            page = await self.browser_no_proxy.newPage()
        except BaseException as e:
            logger.error('创建标签页失败 {}'.format(e))
            return HtmlResponse(url=request.url, request=request, status=status)

        try:
            await asyncio.wait_for(page.setJavaScriptEnabled(True), timeout=5)

            while request_count < 5:

                try:
                    # if request_count in [2, 4]:
                    #     response = await page.goto(request.url, {'timeout': int(50) * 1000, 'waitUntil': 'domcontentloaded'})
                    # else:
                    #     response = await page.goto(request.url, {'timeout': int(50) * 1000, 'waitUntil': 'networkidle0'})
                    # if is_wait:
                    #     await page.waitForNavigation({'timeout': int(50) * 1000, 'waitUntil': 'networkidle0'})
                    response = await page.goto(request.url, {'timeout': int(50) * 1000})
                    page.on('error', self.deal_error)
                    page.on('dialog ', lambda dialog: dialog.dismiss())
                    await asyncio.sleep(30)
                    content = await page.content()
                    status = response.status
                    if status in RETRY_HTTP_CODES:
                        request_count += 1
                        await asyncio.sleep(2)
                    else:
                        cookies = await page.cookies()
                        break
                except BaseException as e:
                    logger.error('页面渲染 goto 失败  {} --> {}'.format(e, request.url))
                    if 'Execution context was destroyed, most likely because of a navigation.' in str(e) or "net::ERR_EMPTY_RESPONSE" in str(e):
                        is_wait = True
                    if 'ERR_NAME_NOT_RESOLVED' in str(e):
                        status = 5004
                        break
                    if 'Protocol error Page.navigate: Target closed.' in str(e):
                        logger.error('协议错误页。导航：目标已关闭。')
                        break
                    if "net::ERR_CONNECTION_TIMED_OUT" in str(e):
                        logger.warning("连接浏览器超时 {}".format(e))
                        break
                    request_count += 1
        except BaseException as e:
            logger.error('标签页设置失败=={}'.format(e))
            return HtmlResponse(url=request.url, request=request, status=status)
        finally:
            try:
                await page.close()
                await self.browser_no_proxy.close()
            except BaseException as e:
                logger.error('页面关闭失败 {}  == {}'.format(e, request.url))

        if status == 304 or status == 412:
            status = 200
        if status != 200:
            logger.error('渲染页面失败 =={} ==url> {} ==seed_url>{}'.format(status, request.url, request.meta.get('seed_url', None)))
            raise IgnoreRequest()
        new_cookies = {}
        for coo in cookies:
            new_cookies[coo["name"]] = coo["value"]
        res = HtmlResponse(url=request.url, body=content.encode(), request=request, status=status)
        res.meta["cookies"] = new_cookies
        self.cookie_dict = new_cookies
        return res

    # @defer.inlineCallbacks
    def process_request(self, request, spider):
        """Check if the Request should be handled by Puppeteer"""

        if request.meta.get('is_renderer', False):
            return as_deferred(self._process_request(request, spider, is_proxy=False))

        if request.meta.get('change_cookie', False):
            request.cookies = self.cookie_dict

    def process_response(self, request, response, spider):
        if response.status == 412:
            # meta = response.get("meta", {})
            # if meta.get("retry_count_", 0) < RETRY_TIMES:
            #     response.meta["retry_count_"] = meta.get("retry_count_", 0) + 1
            return as_deferred(self._process_request(request, spider, is_proxy=False))
        else:
            return response