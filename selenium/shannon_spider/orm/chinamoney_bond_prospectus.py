# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: chinamoney_bond_pdf.py
@time: 2018/10/23 17:50
"""
from sqlalchemy import Column, String
from shannon_spider.db import  ItemBaseModel, CommonFieldMixin

class ChinamoneyBondProspectusItem(CommonFieldMixin, ItemBaseModel):
    ''' 货币网PDF下载结果'''
    __tablename__ = 'chinamoney_bond_prospectus_pdf'
    desc = '货币网募集说明书下载'

    PDF_TITLE = Column(String(200),doc={"zh":"PDF标题"})
    PDF_URL = Column(String(500), doc={"zh": "PDF链接"})
    ANNOUNCEMENT_DATE = Column(String(50),doc={"zh":"公告日期"})

    FILEPATH = Column(String(200),doc={"zh":"文件路径"})
    FILENAME = Column(String(200), doc={"zh": "文件名"})