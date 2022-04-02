from sqlalchemy import Column, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class StatisticsTushareDataItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'tushare'

    date = Column(DATETIME)