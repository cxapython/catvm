# -*- encoding: utf-8 -*-
from sqlalchemy import Column, DateTime, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ChinamoneyIssuerRateItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'chinamoney_issuer_rate'
    desc = 'chinamoney_issuer_rate'

    announcement_title = Column(VARCHAR(500), doc={'zh': '公告标题'})
    publish_date = Column(DateTime, doc={'zh': '公告时间'})
    pdf_url = Column(VARCHAR(2000), doc={'zh': 'pdf链接'})
    FILEPATH = Column(VARCHAR(2000), doc={'zh': 'OSS路径'})