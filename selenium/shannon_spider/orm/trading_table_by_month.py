# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class TradingTableByMonthItem(CommonFieldMixin, ItemBaseModel):
    """海关总署字段"""

    __tablename__ = 'import_export_goods_value_by_month'

    desc = '按月进出口商品总值表'
    # 年度
    YEAR_MONTH = Column(String(20), doc={'zh', '年度'})

    # 进出口
    IMPORT_EXPORT = Column(Numeric(20, 4), doc={'zh', '进出口'})

    # 出口
    EXPORT = Column(Numeric(20, 4), doc={'zh', '出口'})

    # 进口
    IMPORT = Column(Numeric(20, 4), doc={'zh', '进口'})

    # 贸易差额
    TRADE_BALANCE = Column(Numeric(20, 4), doc={'zh', '贸易差额'})

    # 类型
    TYPE = Column(String(20), doc={'zh', '类型'})

    # 类型
    UNIT = Column(String(20), doc={'zh', '单位'})

    # 货币
    CURRENCY = Column(String(20), doc={'zh', '货币'})

