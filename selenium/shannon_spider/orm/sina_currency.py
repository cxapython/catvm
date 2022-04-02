# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SinaCurrencyItem(CommonFieldMixin, ItemBaseModel):
    """新浪汇率字段"""

    __tablename__ = 'sina_currency'

    desc = '新浪汇率'
    # 外汇代码
    CURRENCY_CODE = Column(String(20), doc={'zh', '代码'})

    # 外汇名称
    CURRENCY_SHORT = Column(String(40), doc={'zh', '外汇名称'})

    # 交易日期
    DEAL_DATE = Column(Date, doc={'zh', '交易日期'})

    # 开盘价
    OPEN_PRICE = Column(Numeric(10, 4), doc={'zh', '开盘价'})

    # 收盘价
    CLOSE_PRICE = Column(Numeric(10, 4), doc={'zh', '收盘价'})

    # 最高价
    TOP_PRICE = Column(Numeric(10, 4), doc={'zh', '最高价'})

    # 最低价
    LOW_PRICE = Column(Numeric(10, 4), doc={'zh', '最低价'})

    # 涨跌
    UP_DOWN = Column(Numeric(10, 4), doc={'zh', '涨跌'})

    # 振幅
    AMPLITUDE = Column(Numeric(10, 4), doc={'zh', '振幅'})
