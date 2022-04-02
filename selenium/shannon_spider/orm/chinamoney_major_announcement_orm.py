# encoding: utf-8
'''
@author: zhao zhibo
@file: chinamoney_major_announcement_orm.py
@time: 2021/1/28 下午5:12
@desc:https://tower.im/teams/619394/documents/37852/?fullscreen=false chinamoney_major_announcement
'''
from sqlalchemy import Column, DateTime, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ChinamoneyMajorAnnouncement(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'chinamoney_major_announcement'
    desc = 'chinamoney_major_announcement'

    announcement_title = Column(VARCHAR(500), doc={'zh': '公告标题'})
    publish_date = Column(DateTime, doc={'zh': '公告时间'})
    pdf_url = Column(VARCHAR(2000), doc={'zh': 'pdf链接'})
    FILEPATH = Column(VARCHAR(2000), doc={'zh': 'OSS路径'})