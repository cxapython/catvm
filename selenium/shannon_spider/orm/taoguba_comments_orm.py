# encoding: utf-8
'''
@author: zhao zhibo
@file: taoguba_comments_orm.py
@time: 2021/3/2 下午5:37
@desc:
'''
from sqlalchemy import Column, VARCHAR, DATETIME
from sqlalchemy.dialects.mysql import LONGTEXT

from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class TaogubaCommentsItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'taoguba_comments'

    title = Column(VARCHAR(100), doc={'zh', '标题'})
    content = Column(LONGTEXT, doc={'zh', '内容带标签'})
    web_url = Column(VARCHAR(500), index=True, doc={'zh', '详情页url'})
    author = Column(VARCHAR(100), doc={'zh', '作者'})
    publish_time = Column(DATETIME,  doc={'zh', '作者'})
    source = Column(VARCHAR(100),  doc={'zh', '来源'}, default="淘股吧")