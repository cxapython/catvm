# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class XuangubaoThemeItem(CommonFieldMixin, ItemBaseModel):
    '''选股宝主题舆情'''
    __tablename__ = 'xuangubao_theme_news'
    desc = '选股宝主题舆情'

    THEME = Column(VARCHAR(200), doc={'zh': '概念'})
    TITLE = Column(VARCHAR(500), doc={'zh': '标题'})
    ABSTRACT = Column(VARCHAR(1000), doc={'zh': '摘要'})
    RELEASE_TIME = Column(DATETIME, doc={'zh': '发布时间'})
    CRAWLED_TIME = Column(DATETIME, doc={'zh': '爬取时间'})
