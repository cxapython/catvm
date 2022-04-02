# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN, TEXT, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CompanyMainItem(CommonFieldMixin, ItemBaseModel):
    """东方财富网"""

    __tablename__ = 'company_main_business_crawled'

    desc = '东方财富网'
    # 日期
    END_DT = Column(Date, doc={'zh', '日期'})

    # 公司代码
    COMPANY_CODE = Column(String(40), doc={'zh', '公司代码'})

    # 分类
    CLASS_METHOD = Column(String(40), doc={'zh', '分类'})

    # main_compose
    MAIN_COMPOSE = Column(String(100), doc={'zh', 'main_compose'})

    # main_rev
    MAIN_REV = Column(Numeric(20, 4), doc={'zh', 'main_rev'})

    # rev_proporation
    REV_PROPORATION = Column(Numeric(20, 4), doc={'zh', 'rev_proporation'})

    # main_cost
    MAIN_COST = Column(Numeric(20, 4), doc={'zh', 'main_cost'})

    # cost_proporation
    COST_PROPORATION = Column(Numeric(20, 4), doc={'zh', 'cost_proporation'})

    # main_profit
    MAIN_PROFIT = Column(Numeric(20, 4), doc={'zh', 'main_profit'})

    # profit_proporation
    PROFIT_PROPORATION = Column(Numeric(20, 4), doc={'zh', 'profit_proporation'})

    # margin_rate
    MARGIN_RATE = Column(Numeric(20, 4), doc={'zh', 'margin_rate'})

