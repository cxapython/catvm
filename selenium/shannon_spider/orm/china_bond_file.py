# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN, TEXT, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class BondFileItem(CommonFieldMixin, ItemBaseModel):
    """中国债券信息网"""

    __tablename__ = 'bond_file'

    desc = '中国债券发行文件'
    # 发布日期
    DATETIME = Column(DATETIME, doc={'zh', '发布日期'})

    # 文件标题
    TITLE = Column(TEXT, doc={'zh', '研报标题'})

    # PDF_URL
    PDF_URL = Column(TEXT, doc={'zh', 'PDF_URL'})

    # 存放路径
    PDF_PATH = Column(String(200), doc={'zh', '存放路径'})

    # 是否保存
    IS_DOWNLOADED = Column(BOOLEAN, doc={'zh', '是否存储'})

