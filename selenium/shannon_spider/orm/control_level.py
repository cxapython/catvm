# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.1
@file: control_level.py
@time: 2018/11/20 11:20
控股级别爬取
"""
from sqlalchemy import Column, String, DATETIME
from shannon_spider.db import  CommonFieldMixin, ItemBaseModel


class ControlLevelItem(CommonFieldMixin, ItemBaseModel):
    '''     企业控股的抓取结果'''
    __tablename__ = 'control_relation_crawled'
    desc = '企业控股信息'
    S_INFO_WINDCODE = Column(String(40), doc={"zh": "公司代码"})
    COMPANY_NAME = Column(String(50), doc={"zh": "公司名字"})
    LEVEL = Column(String(20), doc={"zh": "层级"})
    HOLD_COMPANY = Column(String(200), doc={"zh": "持股方"})
    HOLD_RATIO = Column(String(200), doc={"zh": "持股比例"})
    HOLDED_COMPANY = Column(String(100), doc={"zh": "被持股方"})
    UPGRADE_DATE = Column(DATETIME,doc={'zh':'更新日期'})
