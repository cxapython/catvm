# coding=utf-8

from sqlalchemy import Column, VARCHAR, TEXT, Boolean
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class Lang8Item(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'lang8'

    desc = 'lang-8纠错句子'

    USER_ID = Column(VARCHAR(50), doc={'zh': '用户名Id'})
    ARTICLE = Column(VARCHAR(500), doc={'zh': '文章url'})
    LOG_MODIFIER_ID = Column(VARCHAR(50), doc={'zh': '日志评论纠错人ID'})
    ORIGINAL_SENTENCE = Column(VARCHAR(1000), doc={'zh': '原句子'})
    MODIFIER_SENTENCE = Column(VARCHAR(1000), doc={'zh': '修改后句子'})
    DELETE_WORD = Column(VARCHAR(500), doc={'zh': '修改后删除的单词'})
    IS_THANK = Column(Boolean, doc={'zh': '该人的评论是否有收到感谢'})

