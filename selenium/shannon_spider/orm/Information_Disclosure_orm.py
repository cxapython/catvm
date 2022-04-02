# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class InformationDisclosureItem(CommonFieldMixin, ItemBaseModel):
    """
     上交所科创板信息披露
     """
    __tablename__ = 'Information_Disclosure'
    desc = '上交所科创板信息披露'
    ISSUER_NAME = Column(VARCHAR(100), doc={'zh', '发行人'})
    DOCUMENT_NAME = Column(VARCHAR(100), doc={'zh', '文件名称'})
    DATE_PUBLISHED = Column(VARCHAR(100), doc={'zh', '披露日期'})
    FILE_URL = Column(VARCHAR(200), doc={'zh', '文档链接'})
    SAVE_PATH = Column(VARCHAR(200), doc={'zh', '存储路径'})
