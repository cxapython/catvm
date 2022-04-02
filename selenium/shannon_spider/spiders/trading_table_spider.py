# -*- coding: utf-8 -*-

"""
中国海关总署————>进出口商品国别(地区)总值表
"""
# import asyncio
# from twisted.internet import asyncioreactor
# asyncioreactor.install(asyncio.get_event_loop())

import datetime
import re
import scrapy

from shannon_spider.util.notify import send_dingtalk
from shannon_spider.shannon_base_spider import ShannonBaseSpider, ShannonCrawledItem
from shannon_spider.orm.trading_table import TradingTableItem


class TradingTableSpider(ShannonBaseSpider):
    """
    进出口商品国别(地区)总值表
    """
    name = 'trading_table'
    result_orm_model = TradingTableItem
    allowed_domains = ['www.customs.gov.cn']
    base_host = 'http://www.customs.gov.cn'
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

        # 获取所有详情url
        total_urls = []
        for date in range(2019, int(datetime.datetime.now().year) + 1):
            nodes = response.xpath('//*[@class="tbtj{}_tab"]//tr[4]/td[2]/a'.format(date))
            urls = [node.xpath('./@href').extract_first() for node in nodes if node.xpath('./@href').extract_first()]
            total_urls.extend(urls)
        print("----------------------" + str(len(total_urls)))
        for url in total_urls:
            url = self.base_host+url if 'www' not in url else url
            yield scrapy.Request(url=url, callback=self.parse_data, meta={"change_cookie": True})

    def parse_data(self, response):
        """解析数据, 获取详情页信息"""
        # 校验
        if response.status != 200:
            self.logger.error('request: {} bad response status:{}'.format(response.request.url, response.status))
            return False

        # 过滤不需要的数据
        save_index = None
        nodes = response.xpath('//*[@class="easysite-news-text"]/table/tbody/tr')
        title = response.xpath('/html/head/title/text()').extract_first()
        for index, node in enumerate(nodes):
            if node.xpath('./td[1]//text()').extract_first() == '亚洲':
                save_index = index+1
                break

        if not save_index:
            return False

        new_list = []
        for index, node in enumerate(nodes):
            if index+1 < save_index:
                continue
            country = node.xpath('./td[1]//text()').extract_first()
            if not country or '注' in country:
                continue
            item = dict()
            item_2 = dict()
            date = re.search(r'.*?(\w+)年(\w+)月.*', title)
            item['YEAR_MONTH'] = '{}年{}月'.format(date.group(1), date.group(2))
            item['COUNTRY'] = node.xpath('./td[1]//text()').extract_first()
            item['IMPORT_EXPORT'] = node.xpath('./td[2]//text()').extract_first()
            item['EXPORT'] = node.xpath('./td[4]//text()').extract_first()
            item['IMPORT'] = node.xpath('./td[6]//text()').extract_first()
            item['TRADE_BALANCE'] = None
            item['TYPE'] = '当期值'
            item['UNIT'] = '万' if '人民币' in title else '千'
            item['CURRENCY'] = '人民币' if '人民币' in title else '美元'

            item_2['YEAR_MONTH'] = '{}年{}月'.format(date.group(1), date.group(2))
            item_2['COUNTRY'] = node.xpath('./td[1]//text()').extract_first()
            item_2['IMPORT_EXPORT'] = node.xpath('./td[3]//text()').extract_first()
            item_2['EXPORT'] = node.xpath('./td[5]//text()').extract_first()
            item_2['IMPORT'] = node.xpath('./td[7]//text()').extract_first()
            item_2['TRADE_BALANCE'] = None
            item_2['TYPE'] = '累计值'
            item_2['UNIT'] = '万' if '人民币' in title else '千'
            item_2['CURRENCY'] = '人民币' if '人民币' in title else '美元'
            new_list.append(item)
            new_list.append(item_2)

        # 实例存储
        items = ShannonCrawledItem(self, response)
        for item in new_list:
            item = self.filter_data(item)
            try:
                if item['COUNTRY'] == '\u3000':
                    continue
                if len(item['COUNTRY']) > 15:
                    continue
                if not item['IMPORT_EXPORT'].isdigit():
                    continue
                items['YEAR_MONTH'] = item['YEAR_MONTH']
                items['COUNTRY'] = item['COUNTRY']
                items['IMPORT_EXPORT'] = item['IMPORT_EXPORT']
                items['EXPORT'] = item['EXPORT']
                items['IMPORT'] = item['IMPORT']
                items['TRADE_BALANCE'] = self.count(item['EXPORT'], item['IMPORT'])
                items['TYPE'] = item['TYPE']
                items['UNIT'] = item['UNIT']
                items['CURRENCY'] = item['CURRENCY']
                yield items
            except Exception as e:
                self.logger.error('城市:{}, url:{}, error:{}'.format(item['COUNTRY'], response.url, e))

    def count(self, c_export, c_import):
        """计算差值"""
        if c_export is None and c_import is None:
            return None
        c_export = c_export.replace('\u3000', '')
        c_import = c_import.replace('\u3000', '')
        try:
            diff_val = int(float(c_export)) - int(float(c_import))
        except Exception as e:
            self.logger.error(e)
            diff_val = None
        return diff_val

    @staticmethod
    def filter_data(item):
        """过滤数据"""
        for k, v in item.items():
            if k in ['IMPORT_EXPORT', 'EXPORT', 'IMPORT']:
                if not v:
                    v = '0'
                if '\\' in v:
                    v = v.split('\\')[0]
                if ',' in v:
                    v = v.replace(',', '')
                if '-' == v:
                    v = '0'
                if '\xa0' in v:
                    v = v.replace('\xa0', '')
                if ' ' in v:
                    v = v.replace(' ', '')
                item[k] = v
            else:
                item[k] = v
        return item
