# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class StockCodeItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'stock_code'
    desc = '股票代码'
    
    STOCK_CODE = Column(VARCHAR(10), doc={'zh', '股票代码'})
    crawled_time = Column(DateTime, doc={'zh': '爬取时间'})
