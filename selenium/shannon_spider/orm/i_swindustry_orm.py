# encoding: utf-8
'''
@author: zhao zhibo
@file: i_swindustry_orm.py
@time: 2021/1/11 下午7:27
@desc:
'''

from sqlalchemy import Column, VARCHAR, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ISwindustryOrm(CommonFieldMixin, ItemBaseModel):
    """
    基金概况
    """
    __tablename__ = 'i_swindustry'
    desc = '基金概况'

    industry_name = Column(VARCHAR(40), doc={'zh': '行业分级'})
    level_num = Column(VARCHAR(10), doc={'zh': '级别'})
    company_code = Column(VARCHAR(50), doc={'zh': '基金代码'})
    create_date = Column(DATE, doc={'zh': '更新日期'})
