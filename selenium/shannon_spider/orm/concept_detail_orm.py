# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ConceptDetailItem(CommonFieldMixin, ItemBaseModel):
    """
     概念板块行情
     """
    __tablename__ = 'concept_detail'
    desc = '概念板块明细'

    CONCEPT_CODE = Column(VARCHAR(100), doc={'zh', '概念代码'})
    CONCEPT_NAME = Column(VARCHAR(100), doc={'zh', '概念名称'})
    STOCK_CODE = Column(VARCHAR(100), doc={'zh', '股票代码'})
    STOCK_NAME = Column(VARCHAR(100), doc={'zh', '股票名称'})
    CREATE_TIME = Column(DATE, index=True, doc={'zh', '爬虫时间'})
