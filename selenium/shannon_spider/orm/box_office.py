# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class BoxOfficeItem(CommonFieldMixin, ItemBaseModel):
    """猫眼电影"""

    __tablename__ = 'box_office_crawled'

    desc = '猫眼电影'
    # 影院名称
    CINEMA_NAME = Column(String(50), doc={'zh', '影院名称'})

    # BOX_TIME
    BOX_TIME = Column(Date, doc={'zh', 'BOX_TIME'})

    # BOX_INFO
    BOX_INFO = Column(String(50), doc={'zh', 'BOX_INFO'})

    # VIEW_INFO
    VIEW_INFO = Column(String(50), doc={'zh', 'VIEW_INFO'})

    # AVG_SHOW_VIEW
    AVG_SHOW_VIEW = Column(String(50), doc={'zh', 'AVG_SHOW_VIEW'})

    # AVG_VIEW_BOX
    AVG_VIEW_BOX = Column(String(50), doc={'zh', 'AVG_VIEW_BOX'})

