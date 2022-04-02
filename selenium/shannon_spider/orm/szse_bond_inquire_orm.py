# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime

from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SzseBondInquireItem(CommonFieldMixin, ItemBaseModel):
    '''深交所-债券问询函'''
    __tablename__ = 'szse_bond_inquire'
    desc = '深交所-债券问询函'

    INQUIRE_OBJECT = Column(VARCHAR(500), doc={"zh": "问询对象"})
    INQUIRE_TYPE = Column(VARCHAR(200), doc={"zh": "类型"})
    LETTER_NO = Column(VARCHAR(200), doc={"zh": "函号"})
    TITLE = Column(VARCHAR(500), doc={"zh": "标题"})
    PDF_URL = Column(VARCHAR(2000), doc={"zh": "查看全文对应的原pdf_url"})
    PDF_PATH = Column(VARCHAR(500), doc={"zh": "文件存储地址"})
    LETTER_DATE = Column(DateTime, doc={'zh': '发函日期'})
    INQUIRE_RESPONSE = Column(VARCHAR(500), doc={"zh": "回复"})
    INVOLVED_BONDS = Column(VARCHAR(500), doc={"zh": "涉及债券"})
