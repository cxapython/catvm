# encoding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsPriceInfoItem(CommonFieldMixin, ItemBaseModel):
    '''中概股交易信息的抓取结果'''
    __tablename__ = 'ccs_price_info'
    desc = '中概股交易信息'
    DATE = Column(String(40), doc={'zh': '日期'})
    CODE = Column(String(40), doc={'zh': '股票代码'})
    NAME_CH = Column(String(40), doc={'zh': '股票名称'})
    START_PRICE = Column(String(40), doc={'zh': '开盘价'})
    MAX_PRICE = Column(String(40), doc={'zh': '最高价'})
    MIN_PRICE = Column(String(40), doc={'zh': '最低价'})
    YESTERDAY_PRICE = Column(String(40), doc={'zh': '昨收'})
    NUM_TRANS = Column(String(40), doc={'zh': '成交量'})
    PRICE_TRANS = Column(String(40), doc={'zh': '成交额'})
    SUM_PRICE = Column(String(40), doc={'zh': '成交额'})
    SWING = Column(String(40), doc={'zh': '振幅'})
    CHANGE_RATIO = Column(String(40), doc={'zh': '换手率'})
    STOCK_RATIO = Column(String(40), doc={'zh': '股息率'})
    PE = Column(String(40), doc={'zh': '市盈率'})
    PE_TTM = Column(String(40), doc={'zh': '市盈率TTM'})
    EARN_PER_SHARE = Column(String(40), doc={'zh': '每股收益TTM'})
    PB_RATIO = Column(String(40), doc={'zh': '市净率MRQ'})
    VALUE_PRE_SHARE = Column(String(40), doc={'zh': '每股净资产'})
    ADS = Column(String(40), doc={'zh': 'ADS份数'})



