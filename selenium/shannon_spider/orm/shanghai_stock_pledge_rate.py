# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ShangHaiStockPledgeRateItem(CommonFieldMixin, ItemBaseModel):
    """上海证券交易所质押率"""

    __tablename__ = 'shanghai_stock_pledge_rate_crawled'

    desc = '上海证券交易所质押率'
    # 日期
    TRADE_DT = Column(String(20), doc={'zh': '日期'})

    # 质押率
    PLEDGE_RATE = Column(Numeric(20, 4), doc={'zh': '质押率'})

