# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ProspectusDeclareItem(CommonFieldMixin, ItemBaseModel):
    """中国证券监督管理委员会"""

    __tablename__ = 'prospectus_declare'

    desc = '中国证券监督管理委员会'
    # 索引号
    REFERENCE_NUMBER = Column(String(40), doc={'zh', '索引号'})

    # 分类
    CATEGORY = Column(String(100), doc={'zh', '分类'})

    # 发布机构
    INSTITUTION = Column(String(50), doc={'zh', '发布机构'})

    # 发文日期
    PUBLICATION_DATE = Column(String(40), doc={'zh', '发文日期'})

    # 名称
    PDF_NAME = Column(String(100), doc={'zh', '名称'})

    # 主题词
    THEME = Column(String(100), doc={'zh', 'THEME'})

    # PDF_URL
    PDF_URL = Column(String(200), doc={'zh', 'PDF_URL'})

    # 存放路径
    PDF_PATH = Column(String(200), doc={'zh', '存放路径'})

    # 是否保存
    IS_DOWNLOADED = Column(BOOLEAN, doc={'zh', '是否存储'})

