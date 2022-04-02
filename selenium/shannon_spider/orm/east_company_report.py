# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN, TEXT, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class EastCompanyItem(CommonFieldMixin, ItemBaseModel):
    """东方财富网"""

    __tablename__ = 'east_company_report'

    desc = '公司研报'
    # 发布日期
    DATETIME = Column(DATETIME, doc={'zh', '发布日期'})

    # 研报标题
    TITLE = Column(TEXT, doc={'zh', '研报标题'})

    # 股票名称
    COMPANY_NAME = Column(String(40), doc={'zh', '股票名称'})

    # 股票代码
    STOCK_CODE = Column(String(10), doc={'zh', '股票代码'})

    # 研究机构
    INSTITUTION_NAME = Column(String(40), doc={'zh', '研究机构'})

    # 分析师
    AUTHOR = Column(String(20), doc={'zh', '分析师'})

    # 机构评级
    INVESTMENT_RATING = Column(String(20), doc={'zh', '机构评级'})

    # 公司研究
    CATEGORY = Column(String(40), doc={'zh', '公司研究'})

    # 行业名称
    INDUSTRY_NAME = Column(String(40), doc={'zh', '行业名称'})

    # PDF_URL
    PDF_URL = Column(String(200), doc={'zh', 'PDF_URL'})

    # 存放路径
    PDF_PATH = Column(String(200), doc={'zh', '存放路径'})

    # 是否保存
    IS_DOWNLOADED = Column(BOOLEAN, doc={'zh', '是否存储'})

