# -*- encoding: utf-8 -*-
from sqlalchemy import Column, DateTime, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ShclearingBondRiskItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'shclearing_bond_risk'
    desc = 'shclearing_bond_risk'

    announcement_title = Column(VARCHAR(500), doc={'zh': '公告标题'})
    publish_date = Column(DateTime, doc={'zh': '公告时间'})
    pdf_url = Column(VARCHAR(2000), doc={'zh': 'pdf链接'})
    FILEPATH = Column(VARCHAR(2000), doc={'zh': 'OSS路径'})