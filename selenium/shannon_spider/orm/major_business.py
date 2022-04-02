# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: major_business.py
@time: 2018/11/14 18:15

主营业务
"""

from sqlalchemy import Column,String
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class MajorBusinessItem(CommonFieldMixin, ItemBaseModel):
    """
    港股营业收入构成
    """
    __tablename__ = 'major_business'

    desc = '关于公司主营业务的基本情况'

    S_INFO_WINDCODE = Column(String(60), doc={'zh': '股票代码'})
    COMPANY_NAME = Column(String(60), doc={'zh': '公司简称'})
    MAJOR_BUSINESS_TAG = Column(String(3000), doc={'zh': '主营业务标签'})
    MAJOR_BUSINESS = Column(String(3000), doc={'zh': '主营业务'})
    COMPANY_WEBSITE = Column(String(100), doc={'zh': '公司网站'})