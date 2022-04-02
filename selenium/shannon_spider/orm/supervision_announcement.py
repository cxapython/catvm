# coding=utf-8

from sqlalchemy import Column, VARCHAR, INT, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class SupervisionAnnouncementItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'supervision_announcement'

    SEC_CODE = Column(VARCHAR(100), doc={'zh': '公司代码'})
    SEC_MARKET = Column(VARCHAR(10), doc={'zh': '板块名：可选值["深证主板、创业板、中小板、上证主板"]'})
    SEC_NAME = Column(VARCHAR(100), doc={'zh': '公司简称'})
    ANNOUNCEMENT_DATE = Column(Date, doc={'zh': '发函日期/处理日期  "yy-mm-dd"'})
    SUPERVISION_TYPE = Column(VARCHAR(10), doc={'zh': '函件类别/监管类型 可选["关注函、监管关注、通报批评、公开谴责、公开认定"]'})
    ANNOUNCEMENT_URL = Column(VARCHAR(300), doc={'zh': '函件内容/处理事由/CURL'})
    ANNOUNCEMENT_TITLE = Column(VARCHAR(100), doc={'zh': '对应 announcement_url 的公告标题'})
    RELATED_PARTY = Column(VARCHAR(100), doc={'zh': '深交所无此字段/涉及对象 深交所该字段填NULL'})
    REPLY_URL = Column(VARCHAR(100), doc={'zh': '公司回复/上交所无此字段 上交所该字段填NULL'})
    REPLY_TITLE = Column(VARCHAR(100), doc={'zh': '对应 reply_url 的公司回复标题'})
    FILE_PATH = Column(VARCHAR(300), doc={'zh': 'pdf存储路径'})
    FILE_PATH_REPLY = Column(VARCHAR(300), doc={'zh': '公司回复pdf存储路径'})