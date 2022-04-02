# encoding: utf-8
'''
@author: zhao zhibo
@file: research_report_of_radish_orm.py
@time: 2021/1/6 上午10:29
@desc:
'''

from sqlalchemy import Column, VARCHAR, TEXT, DATETIME
from sqlalchemy.dialects.mysql import LONGTEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ResearchReportOfRadishOrm(CommonFieldMixin, ItemBaseModel):
    """
     研报爬取
     """
    __tablename__ = 'research_report_of_radish'
    desc = '研报爬取'
    title = Column(VARCHAR(500), doc={'zh', '标题'}, index=True)
    datetime = Column(DATETIME, doc={'zh', '发布时间'}, index=True)
    institution_name = Column(VARCHAR(50), doc={'zh', '机构'})
    author = Column(VARCHAR(50), doc={'zh', '作者'})
    type = Column(VARCHAR(100), doc={'zh', 'type'})
    pages = Column(VARCHAR(10), doc={'zh', '页数'})
    PDF_url = Column(VARCHAR(500), doc={'zh', 'PDF的url'})
    filepath = Column(VARCHAR(500), doc={'zh', 'PDF存储路径'})
    category = Column(VARCHAR(50), doc={'zh', '类别'})
    industry_name = Column(VARCHAR(50), doc={'zh', '行业'})
    company_name = Column(VARCHAR(50), doc={'zh', '公司'})
    investment_rating = Column(VARCHAR(50), doc={'zh', '评级'})