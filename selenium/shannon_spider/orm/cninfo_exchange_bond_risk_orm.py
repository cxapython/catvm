# -*- encoding: utf-8 -*-
from sqlalchemy import Column, DateTime, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ExchangeBondRiskItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'exchange_bond_risk'
    desc = 'cninfo债券公告-债券其他公告'

    bond_name = Column(VARCHAR(200), doc={'zh': '债券简称'})
    bond_code = Column(VARCHAR(40), doc={'zh': '债券代码'})
    announcement_title = Column(VARCHAR(500), doc={'zh': '公告标题'})
    publish_date = Column(DateTime, doc={'zh': '公告时间'})
    pdf_url = Column(VARCHAR(2000), doc={'zh': 'pdf链接'})
    FILEPATH = Column(VARCHAR(2000), doc={'zh': 'OSS路径'})
