# -*- encoding: utf-8 -*-

from sqlalchemy import Column, Date, VARCHAR, DECIMAL
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class FundScaleItem(CommonFieldMixin, ItemBaseModel):
    """
    基金规模数据
    """
    __tablename__ = 'fund_scale'
    desc = '基金规模数据'

    FUND_CODE = Column(VARCHAR(10), doc={'zh', '基金代码'})       
    DATE = Column(Date, doc={'zh', '日期'})
    PURCHASE = Column(DECIMAL(10,2), doc={'zh': '期间申购（亿份）'})
    RANSDOM = Column(DECIMAL(10,2), doc={'zh': '期间赎回（亿份）'})
    TOTAL_SHARE = Column(DECIMAL(10,2), doc={'zh': '期末总份额（亿份）'})
    NET_ASSETS = Column(DECIMAL(10,2), doc={'zh': '期末净资产（亿元）'})
