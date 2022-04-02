# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: ccs_institution_share.py
@time: 2018/10/20 11:15

中概股
"""
from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsInstitutionSharePossessionItem(CommonFieldMixin, ItemBaseModel):
    '''东方财富对中概股机构持股情况抓取结果'''
    __tablename__ = 'ccs_institution_share_possession'
    desc = '中概股机构持股数据'
    SECURITYCODE = Column(String(40), doc={'zh': '股票代码'})
    SECURITYSHORTNAME = Column(String(100), doc={'zh': '股票名称'})
    REPORTDATE = Column(String(40), doc={'zh': '日期'})
    ORGNUM = Column(String(40), doc={'zh': '持股总数'})
    SHAREHDNUMSUM = Column(String(40), doc={'zh': '持股总数'})
    SHAREHDRATIOJSSUM = Column(String(40), doc={'zh': '持股比例'})
    NEWORGNUM = Column(String(40), doc={'zh': '新进机构'})
    LONGORGNUM = Column(String(40), doc={'zh': '增持机构'})
    SHORTORGNUM = Column(String(40), doc={'zh': '减持机构'})