# encoding: utf-8
"""
@author: guozhenyu 
@contact: guozhenyu@pku.edu.cn

@version: 1.0
@file: secondary_fund_type.py
@time: 2018/9/12 上午11:31

"""

from sqlalchemy import Column, VARCHAR, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class SecondaryFundType(CommonFieldMixin, ItemBaseModel):
    """
    基金代码
    """
    __tablename__ = 'secondary_fund_type'
    desc = '基金二级分类'

    SECONDARY_FUND_TYPE = Column(VARCHAR(10), doc={'zh', '基金二级分类'})
    FUND_CODES = Column(TEXT, doc={'zh', '基金代码'})