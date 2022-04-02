# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ShiborItem(CommonFieldMixin, ItemBaseModel):
    """Shibor初始数据"""

    __tablename__ = 'shibor'

    desc = '中国外汇交易中心——>历史数据——>初始数据'
    # 日期
    DATE = Column(String(20), doc={'zh', '日期'})

    # O/N
    SHIBOR_ON = Column(Numeric(10, 4), doc={'zh', 'O/N'})

    # 1W
    SHIBOR_1W = Column(Numeric(10, 4), doc={'zh', '1W'})

    # 2W
    SHIBOR_2W = Column(Numeric(10, 4), doc={'zh', '2W'})

    # 1M
    SHIBOR_1M = Column(Numeric(10, 4), doc={'zh', '1M'})

    # 3M
    SHIBOR_3M = Column(Numeric(10, 4), doc={'zh', '3M'})

    # 6M
    SHIBOR_6M = Column(Numeric(10, 4), doc={'zh', '6M'})

    # 9M
    SHIBOR_9M = Column(Numeric(10, 4), doc={'zh', '9M'})

    # 1Y
    SHIBOR_1Y = Column(Numeric(10, 4), doc={'zh', '1Y'})


class ShiborQuotedItem(CommonFieldMixin, ItemBaseModel):
    """Shibor报价数据"""

    __tablename__ = 'shibor_quoted'

    desc = '中国外汇交易中心——>历史数据——>报价数据'
    # 日期
    DATE = Column(String(20), doc={'zh', '日期'})

    # 报价机构
    ORGAN_NAME = Column(String(20), doc={'zh', '报价机构'})

    # O/N
    SHIBOR_ON = Column(Numeric(10, 4), doc={'zh', 'O/N'})

    # 1W
    SHIBOR_1W = Column(Numeric(10, 4), doc={'zh', '1W'})

    # 2W
    SHIBOR_2W = Column(Numeric(10, 4), doc={'zh', '2W'})

    # 1M
    SHIBOR_1M = Column(Numeric(10, 4), doc={'zh', '1M'})

    # 3M
    SHIBOR_3M = Column(Numeric(10, 4), doc={'zh', '3M'})

    # 6M
    SHIBOR_6M = Column(Numeric(10, 4), doc={'zh', '6M'})

    # 9M
    SHIBOR_9M = Column(Numeric(10, 4), doc={'zh', '9M'})

    # 1Y
    SHIBOR_1Y = Column(Numeric(10, 4), doc={'zh', '1Y'})


class ShiborMeanItem(CommonFieldMixin, ItemBaseModel):
    """Shibor报价数据"""

    __tablename__ = 'shibor_mean'

    desc = '中国外汇交易中心——>历史数据——>平均数据'
    # 日期
    DATE = Column(String(20), doc={'zh', '日期'})

    # 均值类型
    MEAN_TYPE = Column(String(20), doc={'zh', '均值类型'})

    # O/N
    SHIBOR_ON = Column(Numeric(10, 4), doc={'zh', 'O/N'})

    # 1W
    SHIBOR_1W = Column(Numeric(10, 4), doc={'zh', '1W'})

    # 2W
    SHIBOR_2W = Column(Numeric(10, 4), doc={'zh', '2W'})

    # 1M
    SHIBOR_1M = Column(Numeric(10, 4), doc={'zh', '1M'})

    # 3M
    SHIBOR_3M = Column(Numeric(10, 4), doc={'zh', '3M'})

    # 6M
    SHIBOR_6M = Column(Numeric(10, 4), doc={'zh', '6M'})

    # 9M
    SHIBOR_9M = Column(Numeric(10, 4), doc={'zh', '9M'})

    # 1Y
    SHIBOR_1Y = Column(Numeric(10, 4), doc={'zh', '1Y'})







