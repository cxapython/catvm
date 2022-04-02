# encoding: utf-8

from sqlalchemy import Column, String, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class GuoziNewsItem(CommonFieldMixin, ItemBaseModel):
    '''国资委新闻的抓取结果'''
    __tablename__ = 'guozi_news'
    desc = '国资委新闻'
    NEWS_URL = Column(String(200), doc={'zh': '新闻的链接'})
    NEWS_TYPE = Column(String(200), doc={'zh': '新闻的类型'})
    NEWS_DATE = Column(Date, doc={'zh': '新闻的日期'})
    IMAGE_URL = Column(String(200), doc={'zh': '图片的链接'})
    CONTENT = Column(String(200), doc={'zh': '新闻的标题'})
