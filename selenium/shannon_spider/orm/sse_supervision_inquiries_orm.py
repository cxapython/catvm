# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SseSupervisionInquiriesItem(CommonFieldMixin, ItemBaseModel):
    '''上交所-监管问询'''
    __tablename__ = 'sse_supervision_inquiries'
    desc = '上交所-监管问询'

    COMPANY_CODE = Column(VARCHAR(500), doc={"zh": "证券代码"})
    COMPANY_SNAME = Column(VARCHAR(500), doc={"zh": "证券简称"})
    LETTER_DATE = Column(DateTime, doc={'zh': '发函日期'})
    SUPERVISION_TYPE = Column(VARCHAR(200), doc={"zh": "监管问询类型"})
    TITLE = Column(VARCHAR(500), doc={"zh": "标题"})
    PDF_URL = Column(VARCHAR(2000), doc={"zh": "文件url"})
    PDF_PATH = Column(VARCHAR(500), doc={"zh": "文件存储地址"})
