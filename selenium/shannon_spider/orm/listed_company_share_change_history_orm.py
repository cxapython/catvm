# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ListedCompanyShareChangeHistoryItem(CommonFieldMixin, ItemBaseModel):
    """
     历史股本变动
     """
    __tablename__ = 'listed_company_share_change_history'
    desc = '历史股本变动'
    SEC_NAME = Column(VARCHAR(100), doc={'zh', '股票代码'})
    SEC_CODE = Column(VARCHAR(100), doc={'zh', '股票简称'})
    REPORT_DATE = Column(VARCHAR(100), doc={'zh', '时间'})
    TOTAL_SHARE = Column(VARCHAR(100), doc={'zh', '总股本'})
    LIMITED_SHARE = Column(VARCHAR(100), doc={'zh', '流通受限股份'})
    UNLIMITED_SHARE = Column(VARCHAR(100), doc={'zh', '已流通股份'})
    UNLIMITED_SHARE_A = Column(VARCHAR(100), doc={'zh', '已上市流通A股'})
    CHANGE_REASON = Column(VARCHAR(300), doc={'zh', '变动原因'})
