# encoding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class IssueAnnItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'chinamoney_issue_ann'
    desc = '中国货币网发行情况公告下载'

    ANN_NAME = Column(String(100), doc={'zh': '公告名称'})
    ANN_DATE = Column(Date, doc={'zh': '公告日期'})
    ANN_TYPE = Column(String(10), doc={'zh': '公告类型'})
    FLAG = Column(BOOLEAN, doc={'zh': '是否是同业存单'})
    FILE_TYPE = Column(String(10), doc={'zh': '文件类型'})
    FILE_URL = Column(String(200), doc={'zh': '文件url'})
    SAVE_PATH = Column(String(200), doc={'zh': '保存路径'})
