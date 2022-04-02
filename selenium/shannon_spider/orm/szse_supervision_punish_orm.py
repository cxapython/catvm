# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SzseSupervisionPunishItem(CommonFieldMixin, ItemBaseModel):
    '''深交所-纪律处分'''
    __tablename__ = 'szse_supervision_punish'
    desc = '深交所-纪律处分'

    COMPANY_CODE = Column(VARCHAR(500), doc={"zh": "公司代码"})
    COMPANY_SNAME = Column(VARCHAR(500), doc={"zh": "公司简称"})
    PUNISH_DATE = Column(DateTime, doc={'zh': '处分日期'})
    PUNISH_TYPE = Column(VARCHAR(200), doc={"zh": "处分类别"})
    TITLE = Column(VARCHAR(500), doc={"zh": "标题"})
    PDF_URL = Column(VARCHAR(2000), doc={"zh": "查看全文对应的原pdf_url"})
    PDF_PATH = Column(VARCHAR(500), doc={"zh": "文件存储地址"})
