# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SzseSupervisionMeasureItem(CommonFieldMixin, ItemBaseModel):
    '''深交所-监管措施'''
    __tablename__ = 'szse_supervision_measure'
    desc = '深交所-监管措施'

    COMPANY_CODE = Column(VARCHAR(500), doc={"zh": "公司代码"})
    COMPANY_SNAME = Column(VARCHAR(500), doc={"zh": "公司简称"})
    SUPERVISION_DATE = Column(DateTime, doc={'zh': '采取监管措施日期'})
    SUPERVISION_TYPE = Column(VARCHAR(200), doc={"zh": "监管措施"})
    PDF_URL = Column(VARCHAR(2000), doc={"zh": "函件内容对应的原pdf_url"})
    PDF_PATH = Column(VARCHAR(500), doc={"zh": "文件存储地址"})
    OBJECTS = Column(VARCHAR(500), doc={"zh": "objects"})
