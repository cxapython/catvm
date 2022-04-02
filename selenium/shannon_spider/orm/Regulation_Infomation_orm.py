# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, TEXT
from sqlalchemy.dialects.mysql import LONGTEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class RegulationInfomationItem(CommonFieldMixin, ItemBaseModel):
    """
     舆情_监管动态爬虫
     """
    __tablename__ = 'Regulation_Infomation'
    desc = '舆情_监管动态爬虫'
    TITLE = Column(VARCHAR(500), doc={'zh', '名称'})
    DATE = Column(VARCHAR(100), doc={'zh', '发布时间'})
    TEXT = Column(LONGTEXT, doc={'zh', '正文内容'})
    URL = Column(VARCHAR(200), doc={'zh', '详情页链接'})
    SOURCE = Column(VARCHAR(100), doc={'zh', '来源'})
    WEB = Column(VARCHAR(100), doc={'zh', '来源网站'})