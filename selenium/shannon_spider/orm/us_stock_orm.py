# coding=utf-8

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class UsStockItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'us_stock'

    desc = '知名美股'

    TIME_NOW = Column(DATETIME, doc={'zh': '数据插入的时间'})
    S_INFO_STOCKCODE = Column(VARCHAR(50), doc={'zh': '股票代码'})
    S_INFO_NAME = Column(VARCHAR(50), doc={'zh': '公司简称'})

