# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.1
@file: national_stats.py
@time: 2018/11/21 18:15

国家统计局
"""

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class NationalStatsItem(CommonFieldMixin, ItemBaseModel):
    """
    国家统计局
    """
    __tablename__ = 'nationalstats'
    desc = '国家统计局数据'

    TABLE_NAME = Column(VARCHAR(100), doc={'zh', '表名称'})
    LEVEL_1 = Column(VARCHAR(100), doc={'zh', '一级标题'})
    LEVEL_2 = Column(VARCHAR(100), doc={'zh', '二级标题'})
    LEVEL_3 = Column(VARCHAR(100), doc={'zh', '三级标题'})
    LEVEL_4 = Column(VARCHAR(100), doc={'zh', '四级标题'})
    REG_CODE = Column(VARCHAR(50), doc={'zh', '地区编码'})
    INDICATOR_NAME = Column(VARCHAR(100), doc={'zh', '指标名称'})
    INDICATOR_TIME = Column(VARCHAR(50), doc={'zh', '指标时间'})
    INDICATOR_VALUE = Column(DECIMAL(35,15), doc={'zh', '指标值'})
    INDICATOR_UNIT = Column(VARCHAR(50), doc={'zh', '指标单位'})
