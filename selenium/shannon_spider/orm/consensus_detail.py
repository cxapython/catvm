# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: consensus_detail.py
@time: 2018/11/13 11:15

东方财富-机构对公司的一致盈利预测
"""

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer,DATE,Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ConsensusDetailItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'consensus_profit_detail_crawled'
    desc = '一致盈利预测'

    S_INFO_WINDCODE = Column(VARCHAR(60),doc={'zh','说明'})
    S_INFO_NAME = Column(VARCHAR(50),doc={'zh','说明'})
    END_DATE = Column(DATE,doc={'zh','说明'})
    ANN_DATE = Column(DATE,doc={'zh','说明'})
    S_INSTITUTIONNAME = Column(VARCHAR(100),doc={'zh','说明'})
    S_ANALYSTNAME = Column(VARCHAR(100),doc={'zh','说明'})
    S_FA_EPS = Column(DECIMAL(50,4),doc={'zh','说明'})
    S_NET_PROFIT = Column(DECIMAL(50,4),doc={'zh','说明'})
    PRED_YEAR = Column(VARCHAR(8),doc={'zh','说明'})
    COMPANY_RATING = Column(VARCHAR(8),doc={'zh','说明'})