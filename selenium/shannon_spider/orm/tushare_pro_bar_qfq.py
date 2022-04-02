# coding=utf-8

from sqlalchemy import Column, CHAR, Numeric, DATETIME, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class TheProBarMarketQfqItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'tushare_pro_bar_qfq'

    desc = 'A股复权行情前复权'

    TS_CODE = Column(CHAR(20), index=True, doc={'zh': '代码'})
    TRADE_DATE = Column(DATE, index=True, doc={'zh': '交易日期'})
    OPEN = Column(Numeric(20, 5), doc={'zh': '开盘价(元)'})
    HIGH = Column(Numeric(20, 5), doc={'zh': '最高价(元)'})
    LOW = Column(Numeric(20, 5), doc={'zh': '最低价(元)'})
    CLOSE = Column(Numeric(20, 5), doc={'zh': '收盘价(元)'})
    PRE_CLOSE = Column(Numeric(20, 5), doc={'zh': '昨收价(元)'})
    CHANGE = Column(Numeric(20, 5), doc={'zh': '涨跌额'})
    PCT_CHG = Column(Numeric(20, 5), doc={'zh': '涨跌幅 '})
    VOL = Column(Numeric(20, 5), doc={'zh': '成交量(手)'})
    AMOUNT = Column(Numeric(20, 5), doc={'zh': '成交金额(千元)'})
    ADJ_FACTOR = Column(Numeric(20, 5), doc={'zh': '复权因子'})
    CREATE_TIME = Column(DATETIME, doc={'zh': '当日日期'})

