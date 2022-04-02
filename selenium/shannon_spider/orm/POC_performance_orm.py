# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class POCPerformanceItem(CommonFieldMixin, ItemBaseModel):
    """
     POC业绩
     """
    __tablename__ = 'POC_performance'
    desc = 'POC业绩'
    STOCK_CODE = Column(VARCHAR(100), doc={'zh', '股票代码'})
    STOCK_ABB = Column(VARCHAR(100), doc={'zh', '股票简称'})
    DATE_AN = Column(VARCHAR(100), doc={'zh', '时间'})
    ITEM = Column(VARCHAR(100), doc={'zh', '指标'})
    VALUE = Column(VARCHAR(100), doc={'zh', '值'})
    COMP_NAME = Column(VARCHAR(100), doc={'zh', '公司名称'})
