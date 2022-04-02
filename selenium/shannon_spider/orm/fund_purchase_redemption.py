# coding: utf-8

from sqlalchemy import Column, String, Date, BOOLEAN, TEXT, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CninfItem(CommonFieldMixin, ItemBaseModel):
    """巨潮资讯-基金公告"""

    __tablename__ = 'fund_purchase_redemption'

    desc = '巨潮资讯-基金公告'
    # 公告时间
    DATETIME = Column(Date, doc={'zh', '公告时间'})

    # 公告标题
    TITLE = Column(TEXT, doc={'zh', '公告标题'})

    # 基金代码
    FUND_CODE = Column(VARCHAR(1000), doc={'zh', '基金代码'})

    # 基金简称
    FUND_SHORTNAME = Column(String(40), doc={'zh', '基金简称'})

    # PDF_URL
    PDF_URL = Column(String(200), doc={'zh', 'PDF_URL'})

    # 存放路径
    PDF_PATH = Column(String(200), doc={'zh', '存放路径'})

    # 是否保存
    IS_DOWNLOADED = Column(BOOLEAN, doc={'zh', '是否存储'})

