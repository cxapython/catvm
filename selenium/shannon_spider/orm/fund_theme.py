# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: fund_theme.py
@time: 2018/11/16 18:15

基金主题
"""

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer,String,Numeric, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class FundThemeItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'fund_theme_crawled'

    desc = '基金主题和持仓比重'
    FUND_CODE = Column(String(40), doc={'zh': '基金代码'})
    THEME_FULL = Column(String(500), doc={'zh': '基金主题（全）'})
    THEME_TYPE = Column(String(20), doc={'zh': '主题类型'})
    THEME = Column(String(20), doc={'zh': '基金主题'})
    CCBZ = Column(Numeric(20, 4), doc={'zh': '持仓比重'})
    SPIDER_TIME = Column(DATE, doc={'zh': '爬取时间'})