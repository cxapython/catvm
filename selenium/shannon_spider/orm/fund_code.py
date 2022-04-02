# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class FundCodeItem(CommonFieldMixin, ItemBaseModel):
    """
    基金代码
    """
    __tablename__ = 'fund_code'
    desc = '基金代码'
    
    FUND_CODE = Column(VARCHAR(10), doc={'zh', '基金代码'})      
