# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DATE, Numeric, BigInteger
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ConceptDailyPriceItem(CommonFieldMixin, ItemBaseModel):
    """
     概念板块行情
     """
    __tablename__ = 'concept_daily_price'
    desc = '概念板块每日行情数据'

    CONCEPT_CODE = Column(VARCHAR(100), doc={'zh', '概念代码  str +.THS'})
    CONCEPT_NAME = Column(VARCHAR(100), doc={'zh', '概念名称'})
    DATE = Column(DATE,doc={'zh': '时间'})
    OPEN = Column(Numeric(20, 2), doc={'zh': '开盘价(元)'})
    CLOSE = Column(Numeric(20, 2), doc={'zh': '收盘价(元)'})
    HIGH = Column(Numeric(20, 2), doc={'zh': '最高价(元)'})
    LOW = Column(Numeric(20, 2), doc={'zh': '最低价(元)'})
    VOL = Column(BigInteger, doc={'zh': '成交量'})
    AMOUNT = Column(BigInteger, doc={'zh': '成交金额'})



