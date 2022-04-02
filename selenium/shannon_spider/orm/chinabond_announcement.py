# coding=utf-8

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ChinabondAnnouncementItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'issue_ann_other_web'
    desc = '中债登爬取关键词列表中所有公告'
    ANN_NAME = Column(VARCHAR(100), doc={'zh': '公告名称 '})
    ANN_DATE = Column(Date, doc={'zh': '公告日期  '})
    ANN_TYPE = Column(VARCHAR(10), doc={'zh': '公告类型'})
    FILE_TYPE = Column(VARCHAR(10), doc={'zh': '文档类型'})
    FILE_SOURCE = Column(VARCHAR(10), doc={'zh': '文档来源'})
    FILE_URL = Column(VARCHAR(1000), doc={'zh': '文档链接'})
    SAVE_PATH = Column(VARCHAR(1000), doc={'zh': '存储路径 '})
