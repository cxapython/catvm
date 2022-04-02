# coding=utf-8

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SzseBondItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'szse_bond'

    desc = '深交所债券'

    BOND_CODE = Column(VARCHAR(100), doc={'zh', '债券代码'})
    BOND_SHORT_NAME = Column(VARCHAR(100), doc={'zh': '债券简称'})
    BOND_FULL_NAME = Column(VARCHAR(200), doc={'zh': '债券全称'})
    ISSUER = Column(VARCHAR(100), doc={'zh': '发行人'})
    BOND_CATEGORY = Column(VARCHAR(100), doc={'zh': '债券类别'})
    EXCHANGE_MARKET = Column(VARCHAR(100), doc={'zh': '交易市场'})


