# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, TEXT, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class QuestMobileItem(CommonFieldMixin, ItemBaseModel):
    """quest_mobile"""

    __tablename__ = 'quest_mobile'

    desc = 'quest_mobile'
    # 发布日期
    DATETIME = Column(Date, doc={'zh', '发布日期'})

    # 研报标题
    TITLE = Column(TEXT, doc={'zh', '研报标题'})

    # 股票名称
    COMPANY_NAME = Column(String(40), doc={'zh', '股票名称'})

    # 研究机构:QuestMobile
    INSTITUTION_NAME = Column(String(40), doc={'zh', '研究机构'})

    # 分析师
    AUTHOR = Column(String(20), doc={'zh', '分析师'})

    # 机构评级
    INVESTMENT_RATING = Column(String(20), doc={'zh', '机构评级'})

    # 行业研究
    CATEGORY = Column(String(40), doc={'zh', '行业研究'})

    # 行业名称
    INDUSTRY_NAME = Column(String(40), doc={'zh', '行业名称'})

    # 摘要
    SUMMARY = Column(TEXT, doc={'zh', '摘要'})

    # PDF_URL
    IMG_URL = Column(TEXT, doc={'zh', 'PDF_URL'})

    # 存放路径
    PDF_PATH = Column(TEXT, doc={'zh', '存放路径'})

    # 是否保存
    IS_DOWNLOADED = Column(BOOLEAN, doc={'zh', '是否存储'})


