# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: ccs_stock_info.py
@time: 2018/10/20 11:15

中概股 股票信息
"""
from sqlalchemy import Column, String, Date,Text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsStockInfoItem(CommonFieldMixin, ItemBaseModel):
    '''东方财富对中概股股票信息抓取结果'''
    __tablename__ = 'ccs_stock_info'
    desc = '中概股股票信息数据'
    CODE = Column(String(20), doc={'zh': '股票代码'})
    NAME_EN = Column(String(100), doc={'zh': '公司名称'})
    NAME_CH = Column(String(100), doc={'zh': '英文名称'})
    CHAIR = Column(String(50), doc={'zh': '主席'})
    SECURITYTYPE = Column(String(30), doc={'zh': '证券类型'})
    TRADEMARKET = Column(String(100), doc={'zh': '上市场所'})
    LISTEDDATE = Column(String(30), doc={'zh': '成立日期'})
    FOUNDDATE = Column(String(30), doc={'zh': '上市日期'})
    INDUSTRY = Column(String(100), doc={'zh': '所属行业'})
    OFFICEADDRESS = Column(Text(), doc={'zh': '办公地址'})
    WEBSITE = Column(String(100), doc={'zh': '公司网站'})
    COMPPROFILE = Column(Text(), doc={'zh': '公司介绍'})
