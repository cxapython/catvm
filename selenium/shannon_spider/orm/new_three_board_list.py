# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: new_three_board_list.py
@time: 2018/12/03 11:15

新三板名单爬取
"""
from sqlalchemy import Column, String, Numeric, Date, Time, Integer,Text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class NewThreeBoardItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'new_three_board_list'

    COMPANY_NAME = Column(String(50), doc={'zh': '股票名称'})
    COMPANY_CODE = Column(String(20), doc={'zh': '股票代码'})
    TRANSFER_TYPE = Column(String(50), doc={'zh': '转让类型'})
    INDUSTRY = Column(String(200), doc={'zh': '所属行业'})
    SECURITY_TRADER = Column(String(150),doc={'zh':'主办券商'})
    REGION = Column(String(50), doc={'zh': '地区'})
