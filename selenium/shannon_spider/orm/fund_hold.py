# encoding: utf-8
"""
@author: guozhenyu 
@contact: guozhenyu@pku.edu.cn

@version: 1.0
@file: fund_hold.py
@time: 2018/9/17 下午2:06

"""

from sqlalchemy import Column, VARCHAR, TEXT, DATE, Numeric, String
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class FundHold(CommonFieldMixin, ItemBaseModel):
    """
    基金持仓
    """
    __tablename__ = 'fund_hold'

    desc = '基金持仓'
    FUND_CODE = Column(String(8), doc={'zh': '基金代码'})
    SHARE_CODE = Column(String(15), doc={'zh': '股票代码'})
    SHARE_NAME = Column(String(200), doc={'zh': '股票名称'})
    NET_VALUE = Column(String(10), doc={'zh': '占净值比例'})
    NUMBER_SHARES = Column(String(20), doc={'zh': '持股数（万股）'})
    VALUE_SHARES = Column(String(20), doc={'zh': '持仓市值（万元）'})
    DEADLINE = Column(DATE, doc={'zh': '截止至'})
