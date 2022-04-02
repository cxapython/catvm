# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.1
@file: ccs_dividend.py
@time: 2018/11/12 11:15

中概股
"""
from sqlalchemy import Column, String, Numeric, Date, Time, Integer,Text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsDividendItem(CommonFieldMixin, ItemBaseModel):
    '''东方财富对中概股分红派息情况抓取结果'''
    __tablename__ = 'ccs_dividend'
    desc = '中概股分红派息数据'
    STOCK_CODE = Column(String(40), doc={'zh': '股票代码'})
    STOCK_NAME = Column(String(40), doc={'zh': '股票名称'})
    DATE = Column(String(40), doc={'zh': '日期'})
    DIVIDENT_SCHEME = Column(String(40), doc={'zh': '分红方式'})
    PROGRAMME_NARR = Column(Text(), doc={'zh': '方案说明'})
    CLOSING_DATE = Column(String(40), doc={'zh': '截止过户日'})
    CASH_RELEASE = Column(String(40), doc={'zh': '现金发放日'})
    EX_DIVIDEND_DATE = Column(String(40), doc={'zh': '除权除息日'})
