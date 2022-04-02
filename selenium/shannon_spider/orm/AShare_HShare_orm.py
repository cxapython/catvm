# encoding: utf-8
from sqlalchemy import Column, VARCHAR, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class AShareHShareOrm(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'AShare_HShare'

    S_INFO_CODE = Column(VARCHAR(20), doc={'zh': 'A股代码'})
    HShare_CODE = Column(VARCHAR(20), doc={'zh': 'H股代码'})
    create_date = Column(Date)
