# -*- coding: utf-8 -*-

"""
中国海关总署————>进出口商品总值表
"""
import asyncio
from twisted.internet import asyncioreactor
# asyncioreactor.install(asyncio.get_event_loop())

import datetime
import re
import scrapy

from shannon_spider.util.notify import send_dingtalk
from shannon_spider.shannon_base_spider import ShannonBaseSpider, ShannonCrawledItem
from shannon_spider.orm.trading_table_by_month import TradingTableByMonthItem
from shannon_spider.db import Session


class TradingTableByMonthSpider(ShannonBaseSpider):
    """
    按月进出口商品总值表
    """
    session = Session()
    name = 'trading_table_by_month'
    result_orm_model = TradingTableByMonthItem
    base_host = 'http://www.customs.gov.cn'
    allowed_domains = ['www.customs.gov.cn']
    start_url = 'http://www.customs.gov.cn/customs/302249/302274/302277/index.html'
    # start_urls = [start_url]
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "shannon_spider.middlewares.PuppeteerMiddleware": 1
        },
        "CONCURRENT_REQUESTS": 1
    }

    def __init__(self, **kwargs):
        """
        初始化 CompanyHolderSpider 时，先初始化它的基类
        """
        ShannonBaseSpider.__init__(self, **kwargs)

    def start_requests(self):

        yield scrapy.Request(self.start_url, meta={"is_renderer": True}, callback=self.parse)

    def parse(self, response):
        """解析数据并构成下一页url"""
        # 校验
        if response.status != 200:
            self.logger.error('request: {} bad response status:{}'.format(response.request.url, response.status))
            return False

        try:
            result = self.session.query(TradingTableByMonthItem).all()
            for i in result:
                self.session.delete(i)
                self.session.commit()
        except Exception as e:
            self.logger.error(e)

        # 获取所有详情url
        total_urls = []
        for date in range(2014, int(datetime.datetime.now().year) + 1):
            nodes = response.xpath('//*[@class="tbtj{}_tab"]/table/tbody/tr[3]/td[2]/a'.format(date))
            urls = [node.xpath('./@href').extract_first() for node in nodes if node.xpath('./@href').extract_first()]
            total_urls.extend(urls)

        if total_urls == []:
            self.logger.error('请求url列表为空')
            return
        for url in total_urls:
            url = self.base_host+url if 'www' not in url else url
            yield scrapy.Request(url=url, callback=self.parse_data, meta={"change_cookie": True})

    def parse_data(self, response):
        """解析数据, 获取详情页信息"""
        # 校验
        if response.status != 200:
            self.logger.error('request: {} bad response status:{}'.format(response.request.url, response.status))
            return None

        # 过滤不需要的数据
        save_index = None
        nodes = response.xpath('//*[@class="easysite-news-text"]/table/tbody/tr')
        title = response.xpath('/html/head/title/text()').extract_first()
        for index, node in enumerate(nodes):
            date = node.xpath('./td[1]//text()').extract_first()
            if date and '.' in date:
                save_index = index+1
                break

        if not save_index:
            return None

        new_list = []
        for index, node in enumerate(nodes):
            date = node.xpath('./td[1]//text()').extract_first()
            if index+1 <= save_index:
                continue
            if date and '注' in date:
                continue
            if date and '.' in date:
                item_1 = dict()
                item_2 = dict()
                item_1['YEAR_MONTH'] = date
                item_1['IMPORT_EXPORT'] = node.xpath('./td[2]//text()').extract_first()
                item_1['EXPORT'] = node.xpath('./td[3]//text()').extract_first()
                item_1['IMPORT'] = node.xpath('./td[4]//text()').extract_first()
                item_1['TRADE_BALANCE'] = None
                item_1['TYPE'] = '当期值'
                item_1['UNIT'] = '百万' if '美元' in title else '亿'
                item_1['CURRENCY'] = '美元' if '美元' in title else '人民币'

                item_2['YEAR_MONTH'] = date
                item_2['IMPORT_EXPORT'] = node.xpath('./td[6]//text()').extract_first()
                item_2['EXPORT'] = node.xpath('./td[7]//text()').extract_first()
                item_2['IMPORT'] = node.xpath('./td[8]//text()').extract_first()
                item_2['TRADE_BALANCE'] = None
                item_2['TYPE'] = '累计值'
                item_2['UNIT'] = '百万' if '美元' in title else '亿'
                item_2['CURRENCY'] = '美元' if '美元' in title else '人民币'
                new_list.append(item_1)
                new_list.append(item_2)

        # 实例存储
        items = ShannonCrawledItem(self, response)
        for item in new_list:
            item = self.filter_data(item)
            try:
                items['YEAR_MONTH'] = item['YEAR_MONTH']
                items['IMPORT_EXPORT'] = item['IMPORT_EXPORT']
                items['EXPORT'] = item['EXPORT']
                items['IMPORT'] = item['IMPORT']
                items['TRADE_BALANCE'] = self.count(item['EXPORT'], item['IMPORT'])
                items['TYPE'] = item['TYPE']
                items['UNIT'] = item['UNIT']
                items['CURRENCY'] = item['CURRENCY']
                self.logger.info('=====数据拼装成功：日期————>{}====='.format(item['YEAR_MONTH']))
                yield items
            except Exception as e:
                send_dingtalk(self.name, '{}'.format(e), response.request.url)
                self.logger.error('=====数据抓取失败：日期————>{}====='.format(item['YEAR_MONTH']))
                self.logger.error(e)

    @staticmethod
    def count(c_export, c_import):
        """计算差值"""
        if not c_export or not c_import:
            return None
        return int(c_export) - int(c_import)

    @staticmethod
    def filter_data(item):
        """重组数据"""
        for key, value in item.items():
            if value:
                try:
                    v = value
                    if ' ' in v:
                        v = v.replace(' ', '')
                    if ',' in v:
                        v = v.replace(',', '')
                    if '\r' in v:
                        v = v.replace('\r', '')
                    if '\t' in v:
                        v = v.replace('\t', '')
                    if '\n' in v:
                        v = v.replace('\n', '')
                    if '&nbsp;' in v:
                        v = v.replace('&nbsp;', '')
                    if '\xa0' in v:
                        v = v.replace('\xa0', '')
                    if '\u3000' in v:
                        v = None
                    item[key] = v
                except TypeError:
                    item[key] = value
            else:
                item[key] = value
        return item






