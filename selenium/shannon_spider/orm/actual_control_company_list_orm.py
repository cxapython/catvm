# coding=utf-8

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class ActualControlItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'actual_control_company_list'

    desc = 'tushare 股票名单'

    STOCKCODE = Column(VARCHAR(50), doc={'zh': '原始代码'})
    STOCKNAME = Column(VARCHAR(50), doc={'zh': '公司名称'})
    CODEANDEX = Column(VARCHAR(40), doc={'zh': '个股代码'})
    TIME = Column(DATETIME, doc={'zh': '更新时间'})
