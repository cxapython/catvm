# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SseSupervisionMeasuresItem(CommonFieldMixin, ItemBaseModel):
    '''上交所-监管措施'''
    __tablename__ = 'sse_supervision_measures'
    desc = '上交所-监管措施'

    COMPANY_CODE = Column(VARCHAR(500), doc={"zh": "证券代码"})
    COMPANY_SNAME = Column(VARCHAR(500), doc={"zh": "证券简称"})
    SUPERVISION_TYPE = Column(VARCHAR(200), doc={"zh": "监管类型"})
    MATTER = Column(TEXT, doc={"zh": "处理事由"})
    PDF_URL = Column(VARCHAR(2000), doc={"zh": "文件url"})
    PDF_PATH = Column(VARCHAR(500), doc={"zh": "文件存储地址"})
    OBJECTS = Column(VARCHAR(500), doc={"zh": "涉及对象"})
    TREATMENT_DATE = Column(DateTime, doc={'zh': '处理日期'})
