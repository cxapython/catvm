# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: sse_announcement_list.py
@time: 2018/10/27 9:50
"""

from sqlalchemy import Column, String, Numeric, Date, Time, Integer,Text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SseAnnouncementListItem(CommonFieldMixin, ItemBaseModel):
    '''上交所公告列表抓取结果'''
    __tablename__ = 'sse_announcement_list'
    desc = '上交所公告列表'
    STOCKCODE = Column(String(30), doc={"zh": "股票代码"})
    STOCKNAME = Column(String(80), doc={"zh": "股票名称"})
    ANNOUNCEMENT_TITLE = Column(String(500), doc={"zh": "公报标题"})
    ANNOUNCEMENT_DATE = Column(String(40), doc={"zh": "公报日期"})
    ANNOUNCEMENT_TYPE = Column(String(80), doc={"zh": "公报类型"})
    PDF_URL = Column(String(150), doc={"zh": "公报PDF链接"})