# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, Integer, Date, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class InternetFinanceFirstItem(CommonFieldMixin, ItemBaseModel):
    """
    互联网金融协会运营信息一
    """
    __tablename__ = 'internet_finance_first'
    desc = '互联网金融协会数据'
    COMPANY_NAME = Column(VARCHAR(100), doc={'zh', '公司名称'})
    SHORT_NAME = Column(VARCHAR(50), doc={'zh', '简称'})
    END_DATE = Column(Date, doc={'zh', '信息截止日期'})
    REPORT_DATE = Column(Date, doc={'zh', '信息报送日期'})
    CREDIT_AMOUNT = Column(VARCHAR(20), doc={'zh', '累计借贷笔数'})
    LOAN_AMOUNT = Column(VARCHAR(20), doc={'zh', '累计出借笔数'})
    CREDIT_MONEY = Column(VARCHAR(20), doc={'zh', '借贷余额'})
    FLAG = Column(BOOLEAN, doc={'zh', '是否作废'})
    CREDIT_MONEY_AMOUNT = Column(VARCHAR(20), doc={'zh', '借贷余额笔数'})
    INTEREST_MONEY = Column(VARCHAR(20), doc={'zh', '利息余额'})
    TOTAL_CHUJIE_AMOUNT = Column(VARCHAR(20), doc={'zh', '累计出借人数量'})
    TOTAL_JIEKUAN_AMOUNT = Column(VARCHAR(20), doc={'zh', '累计借款人数量'})
    CURRENT_CHUJIE_AMOUNT = Column(VARCHAR(20), doc={'zh', '当前出借人数量'})
    CURRENT_JIEKUAN_AMOUNT = Column(VARCHAR(20), doc={'zh', '当前借款人数量'})
    TOPTEN_JIEKUAN_MONEY_RATIO = Column(VARCHAR(20), doc={'zh', '前十大借款人待还金额占比'})
    TOPONE_JIEKUAN_MONEY_RATIO = Column(VARCHAR(20), doc={'zh', '最大单一借款人待还金额占比'})
    INCIDENCE_RELATION_JIEKUAN_MONEY = Column(VARCHAR(20), doc={'zh', '关联关系借款余额'})
    INCIDENCE_RELATION_JIEKUAN_MONEY_AMOUNT = Column(VARCHAR(20), doc={'zh', '关联关系借款余额笔数'})
    PAST_DUE = Column(VARCHAR(20), doc={'zh', '逾期金额'})
    PAST_DUE_AMOUNT = Column(VARCHAR(20), doc={'zh', '逾期笔数'})
    PAST_DUE_NINETY = Column(VARCHAR(20), doc={'zh', '逾期90天（不含）以上金额'})
    PAST_DUE_NINETY_AMOUNT = Column(VARCHAR(20), doc={'zh', '逾期90天(不含)以上笔数(笔)'})
    TOTAL_COMPENSATION_MONEY = Column(VARCHAR(20), doc={'zh', '累计代偿金额'})
    TOTAL_COMPENSATION_AMOUNT = Column(VARCHAR(20), doc={'zh', '累计代偿笔数'})
    PROJECT_PAST_DUE_RATIO = Column(VARCHAR(20), doc={'zh', '项目逾期率'})
    PAST_DUE_RATIO = Column(VARCHAR(20), doc={'zh', '金额逾期率'})
    PERCAPITAL_TOTAL_JIEKUAN_MONEY = Column(VARCHAR(20), doc={'zh', '人均累计借款金额'})
    PERCAPITAL_TOTAL_CHUJIE_MONEY = Column(VARCHAR(20), doc={'zh', '人均累计出借金额'})
    TOPONE_CHUJIE_MONEY_RATIO = Column(VARCHAR(20), doc={'zh', '最大单户出借余额占比'})
    TOPTEN_CHUJIE_MONEY_RATIO = Column(VARCHAR(20), doc={'zh', '最大十户出借余额占比'})
    PROJECT_GRADE_PAST_DUE_RATIO_FIRST = Column(VARCHAR(20), doc={'zh', '项目分级逾期率（90天）'})
    PROJECT_GRADE_PAST_DUE_RATIO_SECOND = Column(VARCHAR(20), doc={'zh', '项目分级逾期率（91-180天）'})
    PROJECT_GRADE_PAST_DUE_RATIO_THIRD = Column(VARCHAR(20), doc={'zh', '项目分级逾期率（180天以上）'})
    MONEY_PAST_DUE_RATIO_FIRST = Column(VARCHAR(20), doc={'zh', '金额分级逾期率（90天）'})
    MONEY_PAST_DUE_RATIO_SECOND = Column(VARCHAR(20), doc={'zh', '金额分级逾期率（91-180天）'})
    MONEY_PAST_DUE_RATIO_THIRD = Column(VARCHAR(20), doc={'zh', '金额分级逾期率（180天以上）'})
