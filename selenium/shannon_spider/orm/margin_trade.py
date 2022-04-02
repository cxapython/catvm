# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: margin_trade.py
@time: 2018/11/14 18:15

深市和上市总市值和流通市值数据
"""

from sqlalchemy import Column,String,Integer,Numeric
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class MarginTradeItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'a_share_market_negotia'
    desc = '两市市场总市值'

    # OBJECT_ID = Column(Integer, primary_key=True)
    TRADE_DT = Column(String(20), doc={'zh': '交易日期'})
    S_MARSUM_EXCHMARKET = Column(String(40), doc={'zh': '交易所英文简称'})
    S_MARSUM_MARKET_VALUE = Column(Numeric(20, 4), doc={'zh': '总市值'})
    S_MARSUM_NEGOTIA_VALUE = Column(Numeric(20, 4), doc={'zh': '总流通市值'})