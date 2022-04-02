# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: ccs_financial_indicator.py
@time: 2018/10/20 11:15

中概股
"""

from sqlalchemy import Column, String, Numeric, Date, Time, Integer,Text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsFinancialIndicatorItem(CommonFieldMixin, ItemBaseModel):
    '''中概股财务分析抓取结果'''
    __tablename__ = 'ccs_financial_indicator'
    desc = '中概股财务分析'
    DATETYPE = Column(String(40),doc = {"zh":"日期类型"})
    REPORTDATE = Column(String(40), doc={"zh": "日期"})
    SECURITYCODE = Column(String(40), doc={"zh": "股票代码"})
    TIMETYPE = Column(String(40), doc={"zh": "财报类型"})
    ENDDATE = Column(String(40), doc={"zh": "年结日"})
    CURRENCY = Column(String(40), doc={"zh": "币种"})
    EBPS = Column(String(40), doc={"zh": "基本每股收益"})
    DBPS = Column(String(40), doc={"zh": "稀疏每股收益"})
    GROSSPROFITMARGIN = Column(String(40), doc={"zh": "销售毛利率"})
    NETPROFIT = Column(String(40), doc={"zh": "销售净利率"})
    ACCOUNTRATE = Column(String(40), doc={"zh": "应收账款周转率(次)"})
    TURNOVERRATE = Column(String(40), doc={"zh": "存货周转率(次)"})
    TOTALRATE = Column(String(40), doc={"zh": "总资产周转率(次)"})
    ACCOUNTDAYS = Column(String(40), doc={"zh": "应收账款周转天数"})
    TURNOVERDAYS = Column(String(40), doc={"zh": "存货周转天数"})
    TOTALDAYS = Column(String(40), doc={"zh": "总资产周转天数"})
    EQUALITYRATE = Column(String(40), doc={"zh": "净资产收益率"})
    NETASSETRATE = Column(String(40), doc={"zh": "总资产净利率"})
    LIQUALITYRATE = Column(String(40), doc={"zh": "流动比率(倍)"})
    QUICKRATIO = Column(String(40), doc={"zh": "速动比率(倍)"})
    CASHRATIO = Column(String(40), doc={"zh": "经营业务现金净额/流动负债"})
    ASSETRATIO = Column(String(40), doc={"zh": "资产负债率"})
    PROPERTYRATIO = Column(String(40), doc={"zh": "产权比率"})

