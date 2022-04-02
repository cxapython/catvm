# encoding: utf-8

from sqlalchemy import Column, String, Numeric, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class LugutongTradeItem(CommonFieldMixin, ItemBaseModel):
    '''保存股票交易的抓取结果'''
    __tablename__ = 'lugutong_trade'
    desc = '陆股通每日交易数据'
    TRADE_DATE = Column(Date, doc={'zh': '交易日期'})
    TRADE_PLACE = Column(String(10), doc={'zh': '交易所'})
    TURNOVER = Column(Numeric(20, 4), doc={'zh': '买入及卖出额'})
    BUY_TRADES = Column(Numeric(20, 4), doc={'zh': '买入额'})
    SELL_TRADES = Column(Numeric(20, 4), doc={'zh': '卖出额'})
    NET_BUY_ = Column(Numeric(20, 4), doc={'zh': '净买入额'})
    DAILY_QUOTA_BALANCE = Column(Numeric(20, 4), doc={'zh': '每日额度余额'})
