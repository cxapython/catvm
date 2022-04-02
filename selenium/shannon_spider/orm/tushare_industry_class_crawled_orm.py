# -*- coding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class TushareIndustryClassItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'tushare_industry_class_crawled'

    desc = 'tushare 申万行业分类'

    index_code = Column(VARCHAR(20), doc={'zh': '行业代码'})
    industry_name = Column(VARCHAR(100), doc={'zh': '行业名称'})
    company_code = Column(VARCHAR(100), doc={'zh': '公司代码'})
    company_name = Column(VARCHAR(100), doc={'zh': '公司名称'})
    in_date = Column(VARCHAR(100), doc={'zh': '纳入日期'})
    out_date = Column(VARCHAR(100), doc={'zh': '剔除日期'})
    creat_date = Column(DATE, doc={'zh': '创建日期'})