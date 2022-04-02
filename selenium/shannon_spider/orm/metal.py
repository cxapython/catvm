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


class MetalItem(CommonFieldMixin, ItemBaseModel):
    """
    我的有色
    """
    __tablename__ = 'metal_price_new'

    # OBJECT_ID = Column(Integer, primary_key=True)
    METAL_NAME = Column(String(10), doc={'zh': '金属名称'})
    CATEGORY_NAME = Column(String(20), doc={'zh': '一级品种名称'})
    SUB_CATEGORY_NAME = Column(String(50), doc={'zh': '二级品种名称'})
    TRADEMARK = Column(String(50), doc={'zh': '牌号'})
    FORM = Column(String(50), doc={'zh': '规格'})
    REGION = Column(String(50), doc={'zh': '地区'})
    LOWEST_PRICE = Column(String(20), doc={'zh': '最低价'})
    MID_PRICE = Column(String(20), doc={'zh': '中间价'})
    HIGHEST_PRICE = Column(String(20), doc={'zh': '最高价'})
    UNIT = Column(String(20), doc={'zh': '单位'})
    CHANGE = Column(String(20), doc={'zh': '涨跌'})
    DATE = Column(String(20), doc={'zh': '日期'})
