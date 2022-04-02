# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SseSupervisionRegulatoryItem(CommonFieldMixin, ItemBaseModel):
    '''上交所-债券监管措施'''
    __tablename__ = 'sse_supervision_regulatory'
    desc = '上交所-债券监管措施'

    SECURITY_CODE = Column(VARCHAR(500), doc={"zh": "证券代码"})
    SECURITY_SNAME = Column(VARCHAR(500), doc={"zh": "证券简称"})
    REGULATION_TYPE = Column(VARCHAR(500), doc={"zh": "监管类型"})
    TITLE = Column(VARCHAR(500), doc={"zh": "标题"})
    OBJECTS = Column(VARCHAR(500), doc={"zh": "涉及对象"})
    DISPOSE_DATE = Column(DateTime, doc={'zh': '处理日期'})
    PDF_URL = Column(VARCHAR(2000), doc={"zh": "文件url"})
    PDF_PATH = Column(VARCHAR(500), doc={"zh": "文件存储地址"})
