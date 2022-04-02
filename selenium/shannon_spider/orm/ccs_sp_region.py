# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: ccs_sp_region.py
@time: 2018/10/20 11:15

中概股
"""
from sqlalchemy import Column, String, Numeric, Date, Time, Integer,Text,BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsSpRegionItem(CommonFieldMixin, ItemBaseModel):
    '''中概股主营业务按地区分类的抓取结果'''
    __tablename__ = 'ccs_sp_region'
    desc = '中概股主营业务按产品分类'
    SECURITYCODE = Column(String(40), doc={"zh": "公司代码"})
    SECURITYSHORTNAME = Column(String(40), doc={"zh": "公司名称"})
    REPORTDATE = Column(String(40), doc={"zh": "日期"})
    REGIONNAME = Column(String(100), doc={"zh": "地区"})
    MBREVENUE = Column(String(40), doc={"zh": "金额"})
    RATIO = Column(String(40), doc={"zh": "占比"})
