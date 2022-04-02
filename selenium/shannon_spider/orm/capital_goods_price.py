# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: capital_goods_price.py
@time: 2019/01/07 11:15

国家统计局 流通领域重要生产资料市场价格变动情况
"""

from sqlalchemy import Column, String, Numeric, Date, Time, Integer,Text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CapitalGoodsPriceItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'capital_goods_price'
    desc = '国家统计局流通领域重要生产资料市场价格变动情况'
    CATEGORY = Column(String(20), doc={'zh':'分类'})
    GOODS_NAME = Column(String(50), doc={'zh':'产品名称'})
    UNIT = Column(String(10), doc={'zh':'单位'})
    PRICE = Column(String(20), doc={'zh':'本期价格'})
    CHANGE_VALUE = Column(String(20), doc={'zh':'比上期价格涨跌'})
    CHANGE_RATIO = Column(String(20), doc={'zh':'涨跌幅'})
    TIME = Column(String(20), doc={'zh':'时间'})