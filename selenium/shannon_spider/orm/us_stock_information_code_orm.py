# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class UsStockCodeItem(CommonFieldMixin, ItemBaseModel):
    """
     美股公司股票代码
     """
    __tablename__ = 'us_stock_information_code'
    desc = '美股公司股票代码'

    SECURITYSHORTNAME = Column(VARCHAR(200), doc={'zh', '证券简称'})
    TRADEMARKET = Column(VARCHAR(100), doc={'zh', '上市交易所名称'})
    SECURITYCODE = Column(VARCHAR(100), doc={'zh', '证券代码'})
