# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class NeeqDisclosureItem(CommonFieldMixin, ItemBaseModel):
    '''巨潮资讯新三板定期公告'''
    __tablename__ = 'neeq_disclosure'
    desc = '巨潮资讯新三板定期公告'
    
    STOCK_CODE = Column(VARCHAR(20), doc={'zh': '代码'})
    COMPNAME = Column(VARCHAR(100), doc={'zh': '简称'})
    ANNOUNCEMENT_TITLE = Column(VARCHAR(500), doc={'zh': '公告标题'})
    PUBLISH_DATE = Column(DATETIME, doc={'zh': '公告时间'})
    FILE_URL = Column(VARCHAR(1000), doc={'zh': '文档链接'})
    SAVE_PATH = Column(VARCHAR(1000), doc={'zh': 'OSS路径 '})
