# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ClinicalTrialsItem(CommonFieldMixin, ItemBaseModel):
    """药物临床试验登记与信息公式平台"""

    __tablename__ = 'clinical_trials'

    desc = '临床进度跟踪'
    # 登记号
    REGISTRATION_NUMBER = Column(String(40), doc={'zh', '登记号'})

    # 试验状态
    TEST_STATE = Column(String(20), doc={'zh', '试验状态'})

    # 药物名称
    DRUG_NAME = Column(String(100), doc={'zh', '药物名称'})

    # 适应症
    INDICATIONS = Column(TEXT, doc={'zh', '适应症'})

    # 试验通俗题目
    TEST_SUBJECT = Column(TEXT, doc={'zh', '试验通俗题目'})

    # 申办者联系人
    CONTACTS = Column(String(200), doc={'zh', '申办者联系人'})

    # 申办者名称
    DRUG_COMPANY = Column(String(200), doc={'zh', '申办者名称'})

    # 公示日期
    ANNOUNCEMENT_DATE = Column(Date, doc={'zh', '公示日期'})


