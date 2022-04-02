# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ShuJuJuItem(CommonFieldMixin, ItemBaseModel):
    """数据局字段"""

    __tablename__ = 'shujuju'

    desc = '数据局'
    # 报告时间
    DATE_TIME = Column(Date, doc={'zh', '报告时间'})

    # 标题名称
    TITLE = Column(String(100), doc={'zh', '标题名称'})

    # 机构名称
    INSTITUTION_NAME = Column(String(100), doc={'zh', '机构名称'})

    # 行业研究
    CATEGORY = Column(String(20), doc={'zh', '行业研究'})

    # PDF_URL
    PDF_URL = Column(String(500), doc={'zh', 'PDF_URL'})

    # PDF_PATH
    PDF_PATH = Column(String(500), doc={'zh', 'PDF_PATH'})

    # 是否保存
    IS_DOWNLOADED = Column(BOOLEAN, doc={'zh', '是否存储'})

