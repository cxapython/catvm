# encoding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ZhangtingchiItem(CommonFieldMixin, ItemBaseModel):
    '''选股宝涨停池的抓取结果'''
    __tablename__ = 'zhangtingchi'
    desc = '涨停池每日数据'
    S_INFO_WINDCODE = Column(String(40), doc={'zh': '股票代码'})
    CHANGE_RATE = Column(Numeric(10, 3), doc={'zh': '涨跌幅'})
    BLOCKADE_RATIO = Column(Numeric(10, 3), doc={'zh': '封单比'})
    TURNOVER_RATIO = Column(Numeric(10, 3), doc={'zh': '换手率'})
    FIRST_RAISE_TIME = Column(Time, doc={'zh': '首次封板时间'})
    LAST_RAISE_TIME = Column(Time, doc={'zh': '最后封板时间'})
    OPEN_COUNT = Column(Integer, doc={'zh': '开板数'})
    CONTINUE_BORAD_COUNT = Column(Integer, doc={'zh': '连板数'})
    DATE = Column(Date, doc={'zh': '当日日期'})
