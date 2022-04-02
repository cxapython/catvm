# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class UsStockBasicItem(CommonFieldMixin, ItemBaseModel):
    '''
    美股知名公司基本信息
    '''
    __tablename__ = 'us_stock_information_basic'
    desc = '美股知名公司基本信息'

    SECURITYSHORTNAME = Column(VARCHAR(200), doc={'zh', '证券简称'})
    SECURITYCODE = Column(VARCHAR(200), doc={'zh', '证券代码'})
    SECURITYTYPE = Column(VARCHAR(200), doc={'zh', '证券类型'})
    COMPNAME = Column(VARCHAR(200), doc={'zh', '公司名称'})
    COMPNAMECN = Column(VARCHAR(200), doc={'zh', '中文名称'})
    INDUSTRY = Column(VARCHAR(200), doc={'zh', '所属行业'})
