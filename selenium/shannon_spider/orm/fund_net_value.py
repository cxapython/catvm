# encoding: utf-8
"""
@author: guozhenyu 
@contact: guozhenyu@pku.edu.cn

@version: 1.0
@file: fund_net_value.py
@time: 2018/9/13 上午11:19

"""

from sqlalchemy import Column, VARCHAR, TEXT, DATE, Numeric
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class FundNetValue(CommonFieldMixin, ItemBaseModel):
    """
    基金净值
    """
    __tablename__ = 'fund_net_value'
    desc = '基金二级分类'

    FUND_CODE = Column(VARCHAR(10), doc={'zh': '基金代码'})
    FSRQ = Column(DATE, doc={'zh': '净值日期'})
    DWJZ = Column(Numeric(20, 5), doc={'zh': '单位净值'})
    LJJZ = Column(Numeric(20, 5), doc={'zh': '累计净值'})
    SGZT = Column(VARCHAR(10), doc={'zh':'申购状态'})
    SHZT = Column(VARCHAR(10), doc={'zh':'赎回状态'})
