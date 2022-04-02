# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: national_stats.py
@time: 2018/11/13 18:15

国家统计局
"""

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer,String
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class MineralItem(CommonFieldMixin, ItemBaseModel):
    """
    国家统计局
    """
    __tablename__ = 'mineral_price_crawled'

    # OBJECT_ID = Column(Integer, primary_key=True)
    MINERAL_NAME = Column(String(10), doc={'zh': '矿物名称'})
    CATEGORY_NAME = Column(String(20), doc={'zh': '一级品种名称'})
    SUB_CATEGORY_NAME = Column(String(50), doc={'zh': '二级品种名称'})
    FORM = Column(String(50), doc={'zh': '规格'})
    REGION = Column(String(50), doc={'zh': '地区'})
    PRICE = Column(String(20), doc={'zh': '价格'})
    UNIT = Column(String(20), doc={'zh': '单位'})
    CHANGE = Column(String(20), doc={'zh': '涨跌'})
    DATE = Column(String(20), doc={'zh': '日期'})
    NOTE = Column(String(50), doc={'zh': '备注'})
