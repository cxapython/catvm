# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATE, DECIMAL
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class SSEBondCodeItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'sse_bondcode'
    desc = '上海证券交易所债券代码'
    
    BOND_CODE = Column(VARCHAR(10), doc={'zh', '债券代码'})
    
