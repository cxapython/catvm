# encoding: utf-8
"""
@author: ZhangPei
@file: treasury_yields.py
@time: 2018/8/27 17:24

"""
from sqlalchemy import String, Column, Date, Float, VARCHAR

from shannon_spider.db import ItemBaseModel, CommonFieldMixin


class TreasuryYieldsItem(CommonFieldMixin, ItemBaseModel):
    ''' 国债收益率'''
    __tablename__ = 'treasury_yields'

    TRADE_DATE = Column(Date, doc={'zh': '交易日期'})
    BOND_TYPE = Column(VARCHAR(100), doc={'zh': '债券类型'})
    YIELDS_3_MONTHS = Column(Float, doc={'zh': '3月收益率'})
    YIELDS_6_MONTHS = Column(Float, doc={'zh': '6月收益率'})
    YIELDS_1_YEAR = Column(Float, doc={'zh': '1年收益率'})
    YIELDS_3_YEARS = Column(Float, doc={'zh': '3年收益率'})
    YIELDS_5_YEARS = Column(Float, doc={'zh': '5年收益率'})
    YIELDS_7_YEARS = Column(Float, doc={'zh': '7年收益率'})
    YIELDS_10_YEARS = Column(Float, doc={'zh': '10年收益率'})
    YIELDS_30_YEARS = Column(Float, doc={'zh': '30年收益率'})
