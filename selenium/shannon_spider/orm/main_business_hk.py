# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: main_business_hk.py
@time: 2018/11/13 18:15

营业收入构成
"""

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class MainBusinessHKItem(CommonFieldMixin, ItemBaseModel):
    """
    港股营业收入构成
    """
    __tablename__ = 'company_main_business_hk_crawled'
    desc = '港股营业收入构成'

    END_DT = Column(VARCHAR(20),doc={'zh','日期'})
    S_INFO_WINDCODE = Column(VARCHAR(40),doc={'zh','股票代码'})
    SEGMENT_ITEMCODE = Column(VARCHAR(40),doc={'zh','分类码'})
    SEGMENT_ITEM = Column(VARCHAR(120),doc={'zh','分类'})
    SEGMENT_SALES_RATIO = Column(DECIMAL(20,4),doc={'zh','比例'})