# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: import_class_amount.py
@time: 2018/11/24 18:15

中国海关进口数量和分类
"""

from sqlalchemy import Column, String,Numeric
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ImportClassAmountItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'import_commodities_class_amount'
    desc = '中国海关进口数量和分类'

    YEAR_MONTH = Column(String(20), doc={'zh': '年月'})
    COMMODITY_CLASS = Column(String(100), doc={'zh': '商品总类'})
    COMMODITY_CHAPTER = Column(String(100), doc={'zh': '商品类别'})
    COUNTRY_REGION = Column(String(100), doc={'zh': '国家地区'})
    AMOUNT = Column(Numeric(20, 4), doc={'zh': '数量'})
    TYPE = Column(String(20), doc={'zh': '类型'})
    UNIT = Column(String(20), doc={'zh': '单位'})
    CURRENCY = Column(String(20), doc={'zh': '货币'})