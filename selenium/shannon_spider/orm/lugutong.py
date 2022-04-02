# encoding: utf-8

from sqlalchemy import Column, String, Numeric, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class LugutongItem(CommonFieldMixin, ItemBaseModel):
    '''保存持股数据的抓取结果'''
    __tablename__ = 'lugutong'
    desc = '陆股通每日持股数据'
    TRADE_DATE = Column(Date, doc={'zh': '交易日期'})
    S_INFO_WINDCODE = Column(String(40), doc={'zh': '股票代码'})
    STOCKNUMBER = Column(Numeric(20, 4), doc={'zh': '陆股通持股数'})
