# encoding: utf-8
"""
@author: shanlei mu 
@contact: msl@ruc.edu.cn

@version: 1.0
@file: housing_price.py
@time: 18-8-28 下午4:02

这一行开始写关于本文件的说明与解释
"""

from sqlalchemy import Column, String, Date, Numeric
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class HousingPriceItem(CommonFieldMixin, ItemBaseModel):
    '''中国各城市的抓取结果'''
    __tablename__ = 'housing_price'
    desc = '中国房价信息'
    CITY = Column(String(200), doc={'zh': '城市'})
    DATE = Column(Date, doc={'zh': '日期'})
    HOUSE_TYPE = Column(String(200), doc={'zh': '房子类型'})
    PRICE = Column(Numeric(20, 4), doc={'zh': '价格'})
