# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class FortuneGlobal500HistoryItem(CommonFieldMixin, ItemBaseModel):
    """
     世界500强信息
     """
    __tablename__ = 'Fortune_Global_500'
    desc = '世界500强'
    YEAR = Column(VARCHAR(10), doc={'zh', '排名所属年份'})
    RANK = Column(VARCHAR(10), doc={'zh', '排名'})
    RANK_PREVIOUS_YEAR = Column(VARCHAR(10), doc={'zh', '上年排名'})
    NAME_CN = Column(VARCHAR(100), doc={'zh', '公司名称(中文)'})
    NAME_EN = Column(VARCHAR(100), doc={'zh', '公司名称(英文)'})
    REVENUE = Column(VARCHAR(100), doc={'zh', '营业收入(百万美元)'})
    PROFIT = Column(VARCHAR(100), doc={'zh', '利润(百万美元)'})
    COUNTRY = Column(VARCHAR(100), doc={'zh', '国家'})
