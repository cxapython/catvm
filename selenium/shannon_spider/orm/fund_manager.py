# -*- coding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: fund_manager.py
@time: 2018/11/30 18:15

基金经理信息及其管理过的基金数据
"""

from sqlalchemy import Column, Date, VARCHAR, TEXT, DECIMAL
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class FundManagerItem(CommonFieldMixin, ItemBaseModel):
    """
    基金经理信息及其管理过的基金数据
    """
    __tablename__ = 'fund_manager'
    desc = '基金经理信息及其管理过的基金数据'

    FUND_MANAGER_ID = Column(VARCHAR(10), doc={'zh', '基金经理ID'})
    FUND_MANAGER_NAME = Column(VARCHAR(20), doc={'zh', '基金经理姓名'})     # http://fund.eastmoney.com/manager/30553049.html
    CUMULATIVE_OCCUPIED_TIME = Column(VARCHAR(10), doc={'zh', '累计任职时间'})
    START_OCCUPIED_DATE = Column(Date, doc={'zh', '任职起始日期'})
    CURRENT_FUND_COMPANY = Column(VARCHAR(20), doc={'zh': '现任基金公司'})
    CURRENT_TOTAL_SCALE = Column(DECIMAL(10,2), doc={'zh': '现任基金资产总规模(亿元)'})
    BEST_RATE_OF_RETURN = Column(VARCHAR(10), doc={'zh': '任职期间最佳基金回报率'})
    SELF_INTRODUCTION = Column(TEXT, doc={'zh': '基金经理简介'})
    FUND_CODE = Column(VARCHAR(2000), doc={'zh', '基金代码'})       # 由多个字符串拼接而成，可能会很长，超过最大长度短会报错，所以设的比较大；下同
    FUND_NAME = Column(VARCHAR(4000), doc={'zh', '基金名称'})
    FUND_TYPE = Column(VARCHAR(2000), doc={'zh': '基金类型'})
    FUND_SCALE = Column(VARCHAR(2000), doc={'zh': '规模(亿元)'})
    OCCUPIED_TIME = Column(VARCHAR(5000), doc={'zh': '任职时间'})
    OCCUPIED_DAYS = Column(VARCHAR(2000), doc={'zh': '任职天数'})
    RATE_OF_RETURN = Column(VARCHAR(2000), doc={'zh': '任职期间回报率'})

