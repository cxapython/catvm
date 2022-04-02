# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, JSON
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ChinaBondItem(CommonFieldMixin, ItemBaseModel):
    """中国债券信息"""

    __tablename__ = 'china_bond'

    desc = '中国债券信息'
    # 债券简称
    BOND_SHORT = Column(String(40), doc={'zh', '债券简称'})

    # 债券代码
    BOND_CODE = Column(String(40), doc={'zh', '债券代码'})

    # 发行人简称
    ISSUER = Column(String(40), doc={'zh', '发行人简称'})

    # ISIN
    ISIN = Column(String(40), doc={'zh', 'ISIN码'})

    # 债券全称
    BOND_NAME = Column(String(100), doc={'zh', '债券全称'})

    # 发行日期
    ISSUE_DATE = Column(Date, doc={'zh', '发行日期'})

    # 计划发行量(亿元)
    ISSUE_SUM = Column(Numeric(10, 4), doc={'zh', '计划发行量'})

    # 发行开始日
    ST_ISSUE_TIME = Column(Date, doc={'zh', '发行开始日'})

    # 发行截止日
    EN_ISSUE_TIME = Column(Date, doc={'zh', '发行截止日'})

    # 实际发行量(亿元)
    REAL_ISSUE_SUM = Column(Numeric(10, 4), doc={'zh', '实际发行量'})

    # 付息方式
    PAY_INTEREST_WAY = Column(String(40), doc={'zh', '付息方式'})

    # 选择权类别
    OPTION_TYPE = Column(String(40), doc={'zh', '选择权类别'})

    # 票面利率
    PAY_RATE = Column(Numeric(10, 4), doc={'zh', '票面利率'})

    # 债券期限
    BOND_TM_LIMIT = Column(String(40), doc={'zh', '债券期限'})

    # 起息日
    INTEREST_ST_DATE = Column(Date, doc={'zh', '起息日'})

    # 到期日
    INTEREST_EN_DATE = Column(Date, doc={'zh', '到期日'})

    # 债券信用评级
    BOND_CREDIT_RATE = Column(String(20), doc={'zh', '债券信用评级'})

    # 主体信用评级
    MAIN_CREDIT_RATE = Column(String(20), doc={'zh', '主体信用评级'})

    # 付息频率(月)
    PAY_INTEREST_FRE = Column(String(10), doc={'zh', '付息频率'})

    # 基本利差(%)
    BASIC_RATE_DIFF = Column(Numeric(10, 4), doc={'zh', '基本利差'})

    # 当期基础利率(%)
    THEN_BASIC_RATE = Column(Numeric(10, 4), doc={'zh', '当期基础利率'})

    # 首次划款日
    FIRST_TRANSFER_DATE = Column(Date, doc={'zh', '首次划款日'})

    # 上市流通日
    CIRCULATE_DATE = Column(String(40), doc={'zh', '上市流通日'})

    # 发行手续费率
    ISSUE_PROCEDURE_RATE = Column(Numeric(10, 4), doc={'zh', '发行手续费率'})

    # 兑付手续费率
    CASH_PROCEDURE_RATE = Column(Numeric(10, 4), doc={'zh', '兑付手续费率'})

    # 发行价格
    ISSUE_COST = Column(Numeric(10, 4), doc={'zh', '发行价格'})

    # 参考收益率
    REFER_EARN_RATE = Column(Numeric(10, 4), doc={'zh', '参考收益率'})

    # 下一次赎回日
    NEXT_REDEEM_DATE = Column(Date, doc={'zh', '下一次赎回日'})

    # 债券评级机构
    BOND_ORGAN = Column(String(50), doc={'zh', '债券评级机构'})

    # 主体评级机构
    MAIN_ORGAN = Column(String(50), doc={'zh', '主体评级机构'})

    # 浮动利率基准
    FLOAT_RATE = Column(String(40), doc={'zh', '浮动利率基准'})

    # 剩余本金值
    REMAIN_PRINCIPAL_VALUE = Column(String(40), doc={'zh', '剩余本金值'})





