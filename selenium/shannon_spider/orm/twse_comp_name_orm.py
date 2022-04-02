# -*- coding: utf-8 -*-
from sqlalchemy import Column, Numeric, VARCHAR, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class TwseCompNameItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'twse_comp_name'

    desc = '台湾上市公司的证券代码、证券简称、证券全称、上市买卖日期'

    S_INFO_CODE = Column(VARCHAR(50), doc={'zh': '证券代码'})
    S_SHORTNAME = Column(VARCHAR(100), doc={'zh': '证券简称'})
    COMP_FULLNAME = Column(VARCHAR(200), doc={'zh': '公司全称'})
    S_INFO_LISTDATE = Column(VARCHAR(50), doc={'zh': '上市买卖日期'})
