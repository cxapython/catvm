# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ResearchReportTextItem(CommonFieldMixin, ItemBaseModel):
    """
     研报全文
     """
    __tablename__ = 'research_report_text'
    desc = '研报全文'
    TITLE = Column(VARCHAR(500), doc={'zh', '标题'})
    INSTITUTION = Column(VARCHAR(200), doc={'zh', '机构'})
    AUTHOR = Column(VARCHAR(200), doc={'zh', '研究员'})
    DATE = Column(VARCHAR(100), doc={'zh', '日期'})
    TEXT = Column(TEXT, doc={'zh', '全文'})
    CATEGORY = Column(VARCHAR(200), doc={'zh', '类型'})