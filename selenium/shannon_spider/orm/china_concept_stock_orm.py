# coding=utf-8

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ChinaConceptStockItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'china_concept_stock'

    desc = '中概股'
    TIME_NOW = Column(DATETIME, doc={'zh': '数据插入的时间'})
    S_INFO_STOCKCODE = Column(VARCHAR(50), doc={'zh': '股票代码'})
    S_INFO_NAME = Column(VARCHAR(50), doc={'zh': '公司简称'})

