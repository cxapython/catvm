# coding=utf-8

from sqlalchemy import Column, CHAR, Numeric, DATETIME, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class TushareMonthlyItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'tushare_monthly'

    desc = 'tushare 月K线'

    TS_CODE = Column(CHAR(20), index=True, doc={'zh': '个股代码'})
    TRADE_DATE = Column(DATE, index=True, doc={'zh': '交易日期'})
    OPEN = Column(Numeric(20, 5), doc={'zh': '开盘价(元)'})
    HIGH = Column(Numeric(20, 5), doc={'zh': '最高价(元)'})
    LOW = Column(Numeric(20, 5), doc={'zh': '最低价(元)'})
    CLOSE = Column(Numeric(20, 5), doc={'zh': '收盘价(元)'})
    PRE_CLOSE = Column(Numeric(20, 5), doc={'zh': '昨收价(元)'})
    CHANGE = Column(Numeric(20, 5), doc={'zh': '涨跌额'})
    PCT_CHG = Column(Numeric(20, 5), doc={'zh': '涨跌幅 '})
    VOL = Column(Numeric(20, 5), doc={'zh': '成交额'})
    AMOUNT = Column(Numeric(20, 5), doc={'zh': '成交量'})
    ADJ = Column(CHAR(20), index=True, doc={'zh': '复权类型'})
    ADJ_FACTOR = Column(Numeric(20, 5), doc={'zh': '复权因子'})
    CREATE_TIME = Column(DATETIME, doc={'zh': '创建时间'})

