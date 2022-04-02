# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SseSupervisionDynamicItem(CommonFieldMixin, ItemBaseModel):
    '''上交所-监管动态'''
    __tablename__ = 'sse_supervision_dynamic'
    desc = '上交所-监管动态'

    TITLE = Column(VARCHAR(500), doc={"zh": "标题"})
    CONTENT = Column(TEXT, doc={"zh": "内容"})
    ATTACHMENT_TITLE = Column(VARCHAR(500), doc={"zh": "附件标题"})
    ATTACHMENT_URL = Column(VARCHAR(2000), doc={"zh": "附件链接"})
    ATTACHMENT_PATH = Column(VARCHAR(500), doc={"zh": "附件下载地址"})
    PUBLISH_DATE = Column(DateTime, doc={'zh': '发布时间'})
    WEB_URL = Column(VARCHAR(2000), doc={"zh": "网页地址"})
