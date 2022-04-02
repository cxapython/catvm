# -*- coding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: import_class_amount.py
@time: 2018/10/23 20:15

中国海关进口数量和分类
"""

import re
import asyncio
import time

import scrapy
import traceback

from twisted.internet.defer import Deferred

from shannon_spider.orm.import_class_amount import ImportClassAmountItem
from shannon_spider.shannon_base_spider import ShannonBaseSpider, ShannonCrawledItem


class ImportClassAmountSpider(ShannonBaseSpider):
    # 以下是基类定义的属性
    name = 'import_class_amount'
    result_orm_model = ImportClassAmountItem

    start_url = "http://www.customs.gov.cn/customs/302249/302274/302277/index.html"
    # start_urls = ['http://www.customs.gov.cn/customs/302249/302274/302277/index.html']
    path_list = [
        '//*[@id="ess_ContentPane"]/table[2]/tbody/tr/td/div[1]/div/div/div[3]/table/tbody/tr[4]/td[2]/a[{}]',  # 2018,2019, 2020年进出口商品国别(地区)总值表 人民币
        '//*[@id="ess_ContentPane"]/table[2]/tbody/tr/td/div[1]/div/div/div[3]/table/tbody/tr[18]/td[2]/a[{}]',  # 2018,2019,2020年自部分国家(地区)进口商品类章金额表 人民币
        '//*[@id="ess_ContentPane"]/table[2]/tbody/tr/td/div[1]/div/div/div[4]/table/tbody/tr[4]/td[2]/a[{}]',  # 2018,2019,2020年进出口商品国别(地区)总值表 美元
        '//*[@id="ess_ContentPane"]/table[2]/tbody/tr/td/div[1]/div/div/div[4]/table/tbody/tr[18]/td[2]/a[{}]',  # 2018,2019,2020年自部分国家(地区)进口商品类章金额表 美元

        # '//*[@id="ess_ctr195984_HtmlModule_lblContent"]/div/div[3]/table/tbody/tr[4]/td[2]/a[{}]',  # 2017年进出口商品国别(地区)总值表 人民币
        # '//*[@id="ess_ctr195984_HtmlModule_lblContent"]/div/div[3]/table/tbody/tr[18]/td[2]/a[{}]',  # 2017年自部分国家(地区)进口商品类章金额表 人民币
        # '//*[@id="ess_ctr195984_HtmlModule_lblContent"]/div/div[4]/table/tbody/tr[4]/td[2]/a[{}]',  # 2017年进出口商品国别(地区)总值表 美元
        # '//*[@id="ess_ctr195984_HtmlModule_lblContent"]/div/div[4]/table/tbody/tr[18]/td[2]/a[{}]',  # 2017年自部分国家(地区)进口商品类章金额表 美元
        # '//*[@id="ess_ctr193028_HtmlModule_lblContent"]/div/div[3]/table/tbody/tr[4]/td[2]/a[{}]',  # 2016年进出口商品国别(地区)总值表 人民币
        # '//*[@id="ess_ctr193028_HtmlModule_lblContent"]/div/div[3]/table/tbody/tr[18]/td[2]/a[{}]',  # 2016年自部分国家(地区)进口商品类章金额表 人民币
        # '//*[@id="ess_ctr193028_HtmlModule_lblContent"]/div/div[4]/table/tbody/tr[4]/td[2]/a[{}]',  # 2016年进出口商品国别(地区)总值表 美元
        # '//*[@id="ess_ctr193028_HtmlModule_lblContent"]/div/div[4]/table/tbody/tr[18]/td[2]/a[{}]',  # 2016年自部分国家(地区)进口商品类章金额表 美元
        # '//*[@id="ess_ctr187744_HtmlModule_lblContent"]/div/div[3]/table/tbody/tr[4]/td[2]/a[{}]',  # 2015年进出口商品国别(地区)总值表 人民币
        # '//*[@id="ess_ctr187744_HtmlModule_lblContent"]/div/div[3]/table/tbody/tr[18]/td[2]/a[{}]',  # 2015年自部分国家(地区)进口商品类章金额表 人民币
        # '//*[@id="ess_ctr187744_HtmlModule_lblContent"]/div/div[4]/table/tbody/tr[4]/td[2]/a[{}]',  # 2015年进出口商品国别(地区)总值表 美元
        # '//*[@id="ess_ctr187744_HtmlModule_lblContent"]/div/div[4]/table/tbody/tr[18]/td[2]/a[{}]',  # 2015年自部分国家(地区)进口商品类章金额表 美元
        # '//*[@id="ess_ctr183508_HtmlModule_lblContent"]/div/div[3]/table/tbody/tr[4]/td[2]/a[{}]',  # 2014年进出口商品国别(地区)总值表 人民币
        # '//*[@id="ess_ctr183508_HtmlModule_lblContent"]/div/div[3]/table/tbody/tr[18]/td[2]/a[{}]',  # 2014年自部分国家(地区)进口商品类章金额表 人民币
        # '//*[@id="ess_ctr183508_HtmlModule_lblContent"]/div/div[4]/table/tbody/tr[4]/td[2]/a[{}]',  # 2014年进出口商品国别(地区)总值表 美元
        # '//*[@id="ess_ctr183508_HtmlModule_lblContent"]/div/div[4]/table/tbody/tr[18]/td[2]/a[{}]',  # 2014年自部分国家(地区)进口商品类章金额表 美元
        ]

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "shannon_spider.middlewares.PuppeteerMiddleware": 1
        },
        "CONCURRENT_REQUESTS": 1,
        "DOWNLOAD_DELAY": 1
    }

    def __init__(self, **kwargs):
        ShannonBaseSpider.__init__(self, **kwargs)
        self.a = 0

    def start_requests(self):
        yield scrapy.Request(self.start_url, meta={"is_renderer": True}, callback=self.parse)

    def parse(self, response):
        for path in self.path_list:
            for i in range(1, 13):
                xpath_ = path.format(i)
                links = response.xpath(xpath_ + '/@href').extract()
                if links:
                    for link in links:
                        url = self.format_url(link)
                        yield scrapy.Request(url=url, callback=self.parse_detail, meta={"change_cookie": True})

    def parse_detail(self, response):
        self.a += 1
        print(f"----------------{self.a}")
        root = response
        try:
            title = root.xpath('//*[@id="7be43fc69faa445db008ba24e197b0fc"]/div[2]/div/div/div[1]/h2/text()').extract_first()
        except Exception as e:
            self.logger.warning("Response content isn't text", e)
            return
        res = []
        if title and '进出口' in title:
            pattern = re.compile('）(.*?)进出口')
            date_ = re.findall(pattern, title)
            date_ = date_[0]
            if '人民币' in title:
                currency = '人民币'
            else:
                currency = '美元'

            if root.xpath('//*[@id="easysiteText"]/table/tbody/tr[5]/td[1]/font/b/text()').extract_first():
                i = 4
                while True:
                    i += 1
                    country = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[1]/font/b/text()').extract_first()
                    if not country:
                        break
                    if "1至2月" not in date_:
                        cnr = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[6]/font/text()').extract_first()
                        ljz = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[7]/font/text()').extract_first()
                    elif "1至2月" in date_:
                        cnr = root.xpath(
                            '//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[4]/font/text()').extract_first()
                        ljz = None
                    else:
                        self.logger.error(f"请比对年份结构")
                        return
                    dic = {
                        'date': date_,
                        'class': '总值',
                        'chapter': None,
                        'country': country,
                        'amount_cnr': cnr,
                        'amount_ljz': ljz,
                        'currency': currency
                    }
                    res.append(dic)

            elif root.xpath('//*[@id="easysiteText"]/table/tbody/tr[5]/td[1]/strong/span/span/text()').extract_first():
                i = 4
                while True:
                    i += 1
                    country = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[1]/strong/span/span/text()').extract_first()
                    if not country:
                        break
                    if "1至2月" not in date_:
                        cnr = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[6]/span/span/text()').extract_first()
                        ljz = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[7]/span/span/text()').extract_first()
                    elif "1至2月" in date_:
                        cnr = root.xpath(
                            '//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[4]/span/span/text()').extract_first()
                        ljz = None
                    else:
                        self.logger.error(f"请比对年份结构")
                        return
                    dic = {
                        'date': date_,
                        'class': '总值',
                        'chapter': None,
                        'country': country,
                        'amount_cnr': cnr,
                        'amount_ljz': ljz,
                        'currency': currency
                    }
                    res.append(dic)

            elif root.xpath('//*[@id="easysiteText"]/table/tbody/tr[5]/td[1]/text()').extract_first():
                i = 4
                while True:
                    i += 1
                    country = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[1]/text()').extract_first()
                    if not country:
                        break
                    if "1至2月" not in date_:
                        cnr = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[6]/text()').extract_first()
                        ljz = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[7]/text()').extract_first()
                    elif "1至2月" in date_:
                        cnr = root.xpath(
                            '//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[4]/text()').extract_first()
                        ljz = None
                    else:
                        self.logger.error(f"请比对年份结构")
                        return
                    dic = {
                        'date': date_,
                        'class': '总值',
                        'chapter': None,
                        'country': country,
                        'amount_cnr': cnr,
                        'amount_ljz': ljz,
                        'currency': currency
                    }
                    res.append(dic)

            elif root.xpath('//*[@id="easysiteText"]/table/tbody/tr[5]/td[1]/b/text()').extract_first():
                i = 4
                while True:
                    i += 1
                    country = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[1]/b/text()').extract_first()
                    if not country:
                        break
                    if "1至2月" not in date_:
                        cnr = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[6]/text()').extract_first()
                        ljz = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[7]/text()').extract_first()
                    elif "1至2月" in date_:
                        cnr = root.xpath(
                            '//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[4]/text()').extract_first()
                        ljz = None
                    else:
                        self.logger.error(f"请比对年份结构")
                        return
                    dic = {
                        'date': date_,
                        'class': '总值',
                        'chapter': None,
                        'country': country,
                        'amount_cnr': cnr,
                        'amount_ljz': ljz,
                        'currency': currency
                    }
                    res.append(dic)

            elif root.xpath('//*[@id="easysiteText"]/div/table/tbody/tr[5]/td[1]/text()').extract_first():
                i = 4
                while True:
                    i += 1
                    country = root.xpath('//*[@id="easysiteText"]/div/table/tbody/tr[' + str(i) + ']/td[1]/text()').extract_first()
                    if not country:
                        break
                    if "1至2月" not in date_:
                        cnr = root.xpath('//*[@id="easysiteText"]/div/table/tbody/tr[' + str(i) + ']/td[6]/text()').extract_first()
                        ljz = root.xpath('//*[@id="easysiteText"]/div/table/tbody/tr[' + str(i) + ']/td[7]/text()').extract_first()
                    elif "1至2月" in date_:
                        cnr = root.xpath(
                            '//*[@id="easysiteText"]/div/table/tbody/tr[' + str(i) + ']/td[4]/text()').extract_first()
                        ljz = None
                    else:
                        self.logger.error(f"请比对年份结构")
                        return
                    dic = {
                        'date': date_,
                        'class': '总值',
                        'chapter': None,
                        'country': country,
                        'amount_cnr': cnr,
                        'amount_ljz': ljz,
                        'currency': currency
                    }
                    res.append(dic)

                # //*[@id="easysiteText"]/table/tbody/tr['+str(i)+']/td[1]/font/b/text()
                # //*[@id="easysiteText"]/table/tbody/tr['+str(i)+']/td[1]/strong/span/span/text()
                # //*[@id="easysiteText"]/table/tbody/tr[4]/td[1]
                # //*[@id="easysiteText"]/table/tbody/tr[4]/td[1]/b
                # //*[@id="easysiteText"]/div/table/tbody/tr[4]/td[1]
            else:
                self.logger.error('进出口表数据为空, url:{}'.format(response.url))

        elif title:
            pattern = re.compile('）(.*?)自')
            date_ = re.findall(pattern, title)
            date_ = date_[0]
            class_ = ''
            if '人民币' in title:
                currency = '人民币'
            else:
                currency = ' 美元'

            if root.xpath('//*[@id="easysiteText"]/table/tbody/tr[5]/td[1]/font/b/text()').extract_first():
                i = 4
                while True:
                    i += 1
                    category = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[1]/font/b/text()').extract_first()
                    if not category:
                        break
                    if '第' in category and '类' in category:
                        class_ = category
                    j = 1
                    while True:
                        j += 1
                        country = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[2]/td[' + str(j) + ']/font/b/text()').extract_first()
                        if not country:
                            break
                        if "1至2月" not in date_:
                            cnr = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str((j - 1) * 2) + ']/font/text()').extract_first()
                            ljz = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str((j - 1) * 2 + 1) + ']/font/text()').extract_first()
                        elif "1至2月" in date_:
                            cnr = root.xpath(
                                '//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']/font/text()').extract_first()
                            ljz = None
                        else:
                            self.logger.error(f"请比对年份结构")
                            return
                        if class_ == category:
                            chapter = None
                        else:
                            chapter = category

                        dic = {
                            'date': date_,
                            'class': class_,
                            'chapter': chapter,
                            'country': country,
                            'amount_cnr': cnr,
                            'amount_ljz': ljz,
                            'currency': currency
                        }
                        res.append(dic)

            elif root.xpath('//*[@id="easysiteText"]/table/tbody/tr[5]/td[1]/text()').extract_first():
                i = 4
                while True:
                    i += 1
                    category = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[1]/text()').extract_first()
                    if not category:
                        break
                    if '第' in category and '类' in category:
                        class_ = category
                    j = 1
                    while True:
                        j += 1
                        country = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[2]/td[' + str(j) + ']/text()').extract_first()
                        if not country:
                            break
                        if "1至2月" not in date_:
                            cnr = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str((j - 1) * 2) + ']/text()').extract_first()
                            ljz = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str((j - 1) * 2 + 1) + ']/text()').extract_first()
                        elif "1至2月" in date_:
                            cnr = root.xpath(
                                '//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']/text()').extract_first()
                            ljz = None
                        else:
                            self.logger.error(f"请比对年份结构")
                            return
                        if class_ == category:
                            chapter = None
                        else:
                            chapter = category

                        dic = {
                            'date': date_,
                            'class': class_,
                            'chapter': chapter,
                            'country': country,
                            'amount_cnr': cnr,
                            'amount_ljz': ljz,
                            'currency': currency
                        }
                        res.append(dic)
                    print(i)

            elif root.xpath('//*[@id="easysiteText"]/table/tbody/tr[5]/td[1]/b/text()').extract_first():
                i = 4
                while True:
                    i += 1
                    category = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[1]/b/text()').extract_first()
                    if not category:
                        break
                    if '第' in category and '类' in category:
                        class_ = category
                    j = 1
                    while True:
                        j += 1
                        country = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[2]/td[' + str(j) + ']/b/text()').extract_first()
                        if not country:
                            break
                        if "1至2月" not in date_:
                            cnr = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str((j - 1) * 2) + ']/text()').extract_first()
                            ljz = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str((j - 1) * 2 + 1) + ']/text()').extract_first()
                        elif "1至2月" in date_:
                            cnr = root.xpath(
                                '//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']/text()').extract_first()
                            ljz = None
                        else:
                            self.logger.error(f"请比对年份结构")
                            return
                        if class_ == category:
                            chapter = None
                        else:
                            chapter = category

                        dic = {
                            'date': date_,
                            'class': class_,
                            'chapter': chapter,
                            'country': country,
                            'amount_cnr': cnr,
                            'amount_ljz': ljz,
                            'currency': currency
                        }
                        res.append(dic)

                # //*[@id="easysiteText"]/table/tbody/tr[5]/td[1]/font/b
                # //*[@id="easysiteText"]/table/tbody/tr[5]/td[1]
                # //*[@id="easysiteText"]/table/tbody/tr[4]/td[1]/b
                # //*[@id="easysiteText"]/table/tbody/tr[4]/td[1]/b

            elif root.xpath('//*[@id="easysiteText"]/table/tbody/tr[5]/td[1]//text()').extract_first():
                i = 4
                while True:
                    i += 1
                    category = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[1]//text()').extract_first()
                    if not category:
                        break
                    if '第' in category and '类' in category:
                        class_ = category
                    j = 1
                    while True:
                        j += 1
                        country = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[2]/td[' + str(j) + ']//text()').extract_first()
                        if not country:
                            break
                        if "1至2月" not in date_:
                            cnr = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str((j - 1) * 2) + ']//text()').extract_first()
                            ljz = root.xpath('//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str((j - 1) * 2 + 1) + ']//text()').extract_first()
                        elif "1至2月" in date_:
                            cnr = root.xpath(
                                '//*[@id="easysiteText"]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']//text()').extract_first()
                            ljz = None
                        else:
                            self.logger.error(f"请比对年份结构")
                            return
                        if class_ == category:
                            chapter = None
                        else:
                            chapter = category

                        dic = {
                            'date': date_,
                            'class': class_,
                            'chapter': chapter,
                            'country': country,
                            'amount_cnr': cnr,
                            'amount_ljz': ljz,
                            'currency': currency
                        }
                        res.append(dic)
            else:
                self.logger.error('进口表数据为空, url:{}'.format(response.url))

        for element in res:
            country = self.format_str(element['country'])
            if len(country) > 50:
                continue
            item = ShannonCrawledItem(self, response)
            for tab in range(2):
                try:
                    item['YEAR_MONTH'] = element['date']
                    item['COMMODITY_CLASS'] = self.format_str(element['class'])
                    item['COMMODITY_CHAPTER'] = self.format_str(element['chapter'])
                    item['COUNTRY_REGION'] = country
                    if tab == 0:
                        amount = self.format_str(element['amount_cnr'])
                        if amount:
                            amount = amount.replace(',', '')
                        if amount == "-":
                            amount = None
                        item['AMOUNT'] = amount
                        item['TYPE'] = '当期值'
                    else:
                        if element['amount_ljz'] == None:
                            continue
                        amount = self.format_str(element['amount_ljz'])
                        if amount:
                            amount = amount.replace(',', '')
                        if amount == "-":
                            amount = None
                        item['AMOUNT'] = amount
                        item['TYPE'] = '累计值'
                    if element['currency'] == '人民币':
                        item['UNIT'] = '万'
                    else:
                        item['UNIT'] = '千'
                    item['CURRENCY'] = element['currency']
                except Exception:
                    traceback.print_exc()
                    self.logger.warning('程序遇到了错误...{}...{}...'.format(element['date'],element['class']))
                    continue
                item['is_end'] = False
                yield item
        self.logger.debug("{}数据已成功采集.".format(title))

    def format_url(self, url):
        if 'http' not in url:
            url = 'http://www.customs.gov.cn' + url
        return url

    def format_str(self, strs):
        if strs:
            strs = strs.replace('\xa0', '')
        return strs