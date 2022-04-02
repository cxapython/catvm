# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: ccs_equity.py
@time: 2018/10/20 11:15

中概股
"""
from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsEquityItem(CommonFieldMixin, ItemBaseModel):
    '''东方财富对中概股权益抓取结果'''
    __tablename__ = 'ccs_equity'
    desc = '中概股权益数据'
    CODE = Column(String(40), doc={'zh': '股票代码'})
    NAME = Column(String(40), doc={'zh': '股票名称'})
    REPORTDATE = Column(String(40), doc={'zh': '日期'})
    BEFIOWNER = Column(String(150), doc={'zh': '持股人及持股机构'})
    OWNERSHIPSH = Column(String(40), doc={'zh': '权益股份（股）'})
    OWNERSHIPSHRATE = Column(String(40), doc={'zh': '权益占比'})
    CHGRATIO = Column(String(40), doc={'zh': '变动比例'})
    REPORTERTYPE = Column(String(40), doc={'zh': '报告人类型'})
    STOCKTYPE = Column(String(40), doc={'zh': '股份类型'})