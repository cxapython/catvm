# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: consensus.py
@time: 2018/11/13 11:15

东方财富-机构对公司的一致盈利预测
"""

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer,DATE,Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ConsensusItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'consensus_profit_crawled'
    desc = '一致盈利预测'

    S_INFO_WINDCODE = Column(VARCHAR(60),doc={'zh','说明'})
    S_INFO_NAME = Column(VARCHAR(50),doc={'zh','说明'})
    END_DATE = Column(DATE,doc={'zh','说明'})
    S_FA_EPS = Column(DECIMAL(50,4),doc={'zh','说明'})
    COUNT_S_FA_EPS = Column(Integer,doc={'zh','说明'})
    S_FA_EPS_PRED = Column(DECIMAL(50,4),doc={'zh','说明'})
    COUNT_S_FA_EPS_PRED = Column(Integer,doc={'zh','说明'})
    S_FA_BPS = Column(DECIMAL(50,4),doc={'zh','说明'})
    COUNT_S_FA_BPS = Column(Integer,doc={'zh','说明'})
    S_FA_ROE = Column(DECIMAL(50,4),doc={'zh','说明'})
    COUNT_S_FA_ROE = Column(Integer,doc={'zh','说明'})
    S_FA_EQUITY_NET_PROFIT = Column(DECIMAL(50,4),doc={'zh','说明'})
    COUNT_S_FA_EQUITY_NET_PROFIT = Column(Integer,doc={'zh','说明'})
    TOT_OPER_REV = Column(DECIMAL(50,4),doc={'zh','说明'})
    COUNT_TOT_OPER_REV = Column(Integer,doc={'zh','说明'})
    OPER_PROFIT = Column(DECIMAL(50,4),doc={'zh','说明'})
    COUNT_OPER_PROFIT = Column(Integer,doc={'zh','说明'})
    PRED_YEAR = Column(VARCHAR(8),doc={'zh','说明'})
