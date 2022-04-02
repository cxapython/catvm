# coding=utf-8

from sqlalchemy import Column, CHAR, Numeric, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class TheDailyBasicMarketItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'tushare_daily_basic'

    desc = 'tushare每日指标'

    TS_CODE = Column(CHAR(20), index=True, doc={'zh': '代码'})
    TRADE_DATE = Column(CHAR(8), index=True, doc={'zh': '交易日期'})
    CLOSE = Column(Numeric(20, 5), doc={'zh': '当日收盘价'})
    TURNOVER_RATE = Column(Numeric(20, 5), doc={'zh': '换手率（%）'})
    TURNOVER_RATE_F = Column(Numeric(20, 5), doc={'zh': '换手率（自由流通股）'})
    VOLUME_RATIO = Column(Numeric(20, 5), doc={'zh': '量比'})
    PE = Column(Numeric(20, 5), doc={'zh': '市盈率（总市值/净利润）'})
    PE_TTM = Column(Numeric(20, 5), doc={'zh': '市盈率（TTM）'})
    PB = Column(Numeric(20, 5), doc={'zh': '市净率（总市值/净资产）'})
    PS = Column(Numeric(20, 5), doc={'zh': '市销率'})
    PS_TTM = Column(Numeric(20, 5), doc={'zh': '市销率（TTM）'})
    TOTAL_SHARE = Column(Numeric(20, 5), doc={'zh': '总股本 （万股）'})
    FLOAT_SHARE = Column(Numeric(20, 5), doc={'zh': '流通股本 （万股）'})
    FREE_SHARE = Column(Numeric(20, 5), doc={'zh': '自由流通股本 （万）'})
    TOTAL_MV = Column(Numeric(20, 5), doc={'zh': '总市值 （万元）'})
    CIRC_MV = Column(Numeric(20, 5), doc={'zh': '流通市值（万元）'})
    CREATE_TIME = Column(DATETIME, doc={'zh': '当日日期'})
