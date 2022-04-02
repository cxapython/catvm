# -*- coding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class JqIndustryItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'jq_industry_crawled'

    desc = '聚宽申万行业分类'

    index_code = Column(VARCHAR(20), doc={'zh': '行业代码'})
    industry_name = Column(VARCHAR(100), doc={'zh': '行业名称'})
    level_num = Column(VARCHAR(10), doc={'zh': '级别'})
    company_code = Column(VARCHAR(100), doc={'zh': '公司代码'})
    creat_date = Column(DATETIME, doc={'zh': '创建日期'})
    source = Column(VARCHAR(100), doc={'zh': '数据来源'})
