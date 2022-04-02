# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, Integer, Date, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class InternetFinanceSecondItem(CommonFieldMixin, ItemBaseModel):
    """
    互联网金融协会运营信息二
    """
    __tablename__ = 'internet_finance_second'
    desc = '互联网金融协会数据'

    COMPANY_NAME = Column(VARCHAR(100), doc={'zh', '公司名称'})
    SHORT_NAME = Column(VARCHAR(50), doc={'zh', '简称'})
    END_DATE = Column(Date, doc={'zh', '信息截止日期'})
    TRANSACTION_MONEY = Column(VARCHAR(20), doc={'zh', '交易总额'})
    TRANSACTION_AMOUNT = Column(VARCHAR(20), doc={'zh', '交易总笔数'})
    INVEST_AMOUNT = Column(VARCHAR(20), doc={'zh', '投资总笔数'})
    FINANCE_AMOUNT = Column(VARCHAR(20), doc={'zh', '融资人总数'})
    FLAG = Column(BOOLEAN, doc={'zh', '是否作废'})
    INVESTOR_AMOUNT = Column(VARCHAR(20), doc={'zh', '投资人总数'})
    TOBE_COMPENSATION_MONEY = Column(VARCHAR(20), doc={'zh', '待偿金额'})
    PAST_DUE = Column(VARCHAR(20), doc={'zh', '逾期金额'})
    PROJECT_PAST_DUE_RATIO = Column(VARCHAR(20), doc={'zh', '项目逾期率'})
    PAST_DUE_RATIO = Column(VARCHAR(20), doc={'zh', '金额逾期率'})
    PROJECT_PAST_DUE_AMOUNT = Column(VARCHAR(20), doc={'zh', '逾期项目数'})
    PERCAPITAL_TOTAL_FINANCE_MONEY = Column(VARCHAR(20), doc={'zh', '人均累积融资金额'})
    PERCAPITAL_TOTAL_INVEST_MONEY = Column(VARCHAR(20), doc={'zh', '人均累积投资金额'})
    PER_FINANCE_MONEY = Column(VARCHAR(20), doc={'zh', '笔均融资金额'})
    TOPONE_FINANCE_MONEY_RATIO = Column(VARCHAR(20), doc={'zh', '最大单户融资余额占比'})
    TOPTEN_FINANCE_MONEY_RATIO = Column(VARCHAR(20), doc={'zh', '最大10户融资余额占比'})
    TOPONE_INVEST_MONEY_RATIO = Column(VARCHAR(20), doc={'zh', '最大单户投资余额占比'})
    TOPTEN_INVEST_MONEY_RATIO = Column(VARCHAR(20), doc={'zh', '最大10户投资余额占比'})
    PROJECT_GRADE_PAST_DUE_RATIO_FIRST = Column(VARCHAR(20), doc={'zh', '项目分级逾期率（90天）'})
    PROJECT_GRADE_PAST_DUE_RATIO_SECOND = Column(VARCHAR(20), doc={'zh', '项目分级逾期率（91-180天）'})
    PROJECT_GRADE_PAST_DUE_RATIO_THIRD = Column(VARCHAR(20), doc={'zh', '项目分级逾期率（181天以上）'})
    MONEY_PAST_DUE_RATIO_FIRST = Column(VARCHAR(20), doc={'zh', '金额分级逾期率（90天）'})
    MONEY_PAST_DUE_RATIO_SECOND = Column(VARCHAR(20), doc={'zh', '金额分级逾期率（91-180天）'})
    MONEY_PAST_DUE_RATIO_THIRD = Column(VARCHAR(20), doc={'zh', '金额分级逾期率（181天以上）'})
    HISTORY_PROJECT_PAST_DUE_MONEY = Column(VARCHAR(20), doc={'zh', '历史项目逾期金额'})
    HISTORY_PROJECT_PAST_DUE_RATIO = Column(VARCHAR(20), doc={'zh', '历史项目逾期率'})
    TOTAL_PAST_DUE_COMPENSATION_MONEY = Column(VARCHAR(20), doc={'zh', '累计逾期代偿金额'})
    TOTAL_PAST_DUE_COMPENSATION_AMOUNT = Column(VARCHAR(20), doc={'zh', '累计逾期代偿笔数'})
