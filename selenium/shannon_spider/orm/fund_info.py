# encoding: utf-8
"""
@author: guozhenyu 
@contact: guozhenyu@pku.edu.cn

@version: 1.0
@file: fund_info.py
@time: 2018/9/13 下午7:11

"""

from sqlalchemy import Column, VARCHAR, TEXT, DATE, Numeric, String
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class FundInfo(CommonFieldMixin, ItemBaseModel):
    """
    基金概况
    """
    __tablename__ = 'fund_info'
    desc = '基金概况'

    FUND_CODE = Column(String(40), doc={'zh': '基金代码'})
    FUND_NAME_ABBREVIATION = Column(String(50), doc={'zh': '基金简称'})
    FUND_NAME_FULL = Column(String(50), doc={'zh': '基金全称'})
    FUND_TYPE = Column(String(8), doc={'zh': '基金类型'})
    FUND_SETUP_DATE = Column(DATE, doc={'zh': '成立日期'})
    FUND_SIZE = Column(String(50), doc={'zh': '基金规模'})
    FUND_SIZE_DEADLINE = Column(DATE, doc={'zh': '基金规模最新截止日期'})
    GUANLIREN = Column(String(50), doc={'zh': '管理人'})
    FUND_MANAGER = Column(String(50), doc={'zh': '基金经理'})
    BUSINESS_COMPREF = Column(String(500), doc={'zh': '业绩比较基准'})
    TRACER = Column(String(50), doc={'zh': '跟踪标的'})
