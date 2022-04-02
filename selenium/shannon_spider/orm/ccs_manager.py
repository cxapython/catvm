# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: ccs_manager.py
@time: 2018/10/20 11:15

中概股
"""
from sqlalchemy import Column, String, Numeric, Date, Time, Integer,Text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsManagerItem(CommonFieldMixin, ItemBaseModel):
    '''中概股高管研究的抓取结果'''
    __tablename__ = 'ccs_manager'
    desc = '中概股高管研究'
    SECURITYCODE = Column(String(40), doc={"zh": "公司代码"})
    SECURITYSHORTNAME = Column(String(100), doc={"zh": "公司名称"})
    NAMEEN = Column(String(50), doc={"zh": "高管姓名"})
    SEX = Column(String(40), doc={"zh": "性别"})
    EDUCATION = Column(String(40), doc={"zh": "学历"})
    BIRTHDATE = Column(String(40), doc={"zh": "出生年份"})
    OCCUPATION = Column(Text(), doc={"zh": "任职"})
    RESUME = Column(Text(), doc={"zh": "中文简历"})
    RESUMEEN = Column(Text(), doc={"zh": "英文简历"})

