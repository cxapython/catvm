# -*- coding: utf-8 -*-
from sqlalchemy import Column, Numeric, VARCHAR, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class LuoboSwindexItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'luobo_swindex_crawled'

    desc = '萝卜投研申万行业指数'

    DATE = Column(Date, doc={'zh': '交易日期'})
    INDECODE = Column(VARCHAR(20), doc={'zh': '行业代码'})
    PRECLOSE = Column(Numeric(30, 15), doc={'zh': '前一日收盘价'})
    CLOSE = Column(Numeric(30, 15), doc={'zh': '收盘价'})
    OPEN = Column(Numeric(30, 15), doc={'zh': '开盘价'})
    CHANGE = Column(Numeric(30, 15), doc={'zh': '涨跌额'})
    CHANGEPRECENT = Column(Numeric(30, 15), doc={'zh': '涨跌幅'})
    HIGH = Column(Numeric(30, 15), doc={'zh': '最高价'})
    LOW = Column(Numeric(30, 15), doc={'zh': '最低价'})
    VOLUME = Column(Numeric(30, 15), doc={'zh': '成交量'})
