# -*- coding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class TushareIndustryCodeItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'tushare_industry_code_crawled'

    desc = 'tushare 申万行业分类'

    index_code = Column(VARCHAR(20), doc={'zh': '指数代码'})
    industry_name = Column(VARCHAR(100), doc={'zh': '行业分级'})
    level_num = Column(VARCHAR(10), doc={'zh': '行业级别'})
    creat_date = Column(DATE, doc={'zh': '创建日期'})
