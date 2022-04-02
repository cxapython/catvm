# encoding: utf-8

from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class ChineseCharStrokesItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'chinese_char_strokes'
    desc = '汉字笔顺'

    CHARACTER = Column(VARCHAR(100), doc={'zh':'汉字'})
    STROKES = Column(VARCHAR(500), doc={'zh':'笔顺'})