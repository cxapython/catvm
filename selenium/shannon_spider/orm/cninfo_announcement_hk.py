# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: cninfo_announcement_hk.py
@time: 2018/01/05 21:10
巨潮资讯公告爬取
"""
from sqlalchemy import Column, String, BOOLEAN, DATETIME, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CninfoAnnouncementHKItem(CommonFieldMixin, ItemBaseModel):
    '''巨潮资讯公告列表的抓取结果'''
    __tablename__ = 'cninfo_announcement_hk'
    desc = '巨潮资讯公告列表'
    EXCHANGE = Column(String(50),doc={'zh':'交易所'})
    COMPANY_CODE = Column(String(40), doc={'zh': '公司代码'})
    COMPANY_NAME = Column(String(80), doc={'zh': '公司名称'})
    ANNOUNCEMENT_ID = Column(String(40), doc={'zh': '公告ID'})
    ANNOUNCEMENT_TITLE = Column(String(500), doc={'zh': '公告标题'})
    ANNOUNCEMENT_TIME = Column(DATETIME, doc={'zh': '公告时间'})
    ANNOUNCEMENT_FILE_NAME = Column(String(40), doc={'zh': '公告文件名字'})
    URL = Column(String(150), doc={'zh': 'PDF链接'})
    VIEW_COUNT = Column(Integer, doc={'zh': '浏览次数'})
    FILE_SIZE = Column(String(20), doc={'zh': '文件大小'})
    ANNOUNCEMENT_TYPE = Column(String(50), doc={'zh': '公告类型'})
    ORIGIN_ID = Column(String(20), doc={'zh': '原始ID'})
    CACHE_PDF = Column(BOOLEAN, doc={'zh': 'PDF是否已缓存'})
    FILEPATH = Column(String(250), doc={'zh': 'OSS路径'})