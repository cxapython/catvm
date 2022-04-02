# -*- encoding: utf-8 -*-
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import Column, VARCHAR, DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class XueqiuTodayItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'xueqiu_today'
    desc = '雪球今日话题'

    title = Column(VARCHAR(500), doc={"zh": "标题"})
    content = Column(LONGTEXT, doc={'zh': '内容'})
    author = Column(VARCHAR(200), doc={"zh": "作者"})
    web_url = Column(VARCHAR(500), index=True, doc={"zh": "详情页 url"})
    publish_time = Column(DateTime, doc={"zh": "发表时间"})
    source = Column(VARCHAR(50), doc={"zh": "来源"})
