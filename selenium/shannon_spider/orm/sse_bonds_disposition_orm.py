# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SseBondsDispositionItem(CommonFieldMixin, ItemBaseModel):
    '''上交所-债券纪律处分'''
    __tablename__ = 'sse_bonds_disposition'
    desc = '上交所-债券纪律处分'

    SECURITY_CODE = Column(VARCHAR(500), doc={"zh": "证券代码"})
    SECURITY_SNAME = Column(VARCHAR(500), doc={"zh": "证券简称"})
    TITLE = Column(VARCHAR(500), doc={"zh": "标题"})
    CONTENT = Column(TEXT, doc={"zh": "网页内容"})
    WEB_URL = Column(VARCHAR(500), doc={"zh": "详情页url"})
    DISPOSE_DATE = Column(DateTime, doc={'zh': '处理日期'})
    FILE_URL = Column(VARCHAR(2000), doc={"zh": "文件url"})
    FILE_PATH = Column(VARCHAR(500), doc={"zh": "文件存储地址"})
