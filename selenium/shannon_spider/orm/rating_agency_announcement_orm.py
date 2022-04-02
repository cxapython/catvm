# encoding: utf-8
'''
@author: zhao zhibo
@file: rating_agency_announcement_orm.py
@time: 2021/1/28 上午10:32
@desc:
'''

from sqlalchemy import Column, Date, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class RatingAgencyAnnouncementOrm(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'rating_agency_announcement'

    title = Column(VARCHAR(100), doc={'zh': '标题'})
    ann_date = Column(Date, doc={'zh': '公告日期'})
    pdf_url = Column(VARCHAR(1000), doc={'zh': 'pdf地址'})
    source = Column(VARCHAR(20), doc={'zh': '来源'})
    SAVE_PATH = Column(VARCHAR(1000), doc={'zh': 'OSS路径'})
