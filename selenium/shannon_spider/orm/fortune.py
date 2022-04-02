# encoding: utf-8
from sqlalchemy import Column, String, Numeric, Date, Time, Integer,Text,DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class FortuneItem(CommonFieldMixin, ItemBaseModel):
    """
    fortune网站爬虫数据表结构
    """
    __tablename__ = "fortune"
    desc = "fortune网站文章"
    TITLE = Column(String(200), doc={"zh": "文章标题"})
    AUTHOR = Column(String(80), doc={"zh": "文章作者"})
    CONTENT = Column(Text, doc={"zh": "文章内容"})
    TRANSLATE = Column(Text, doc={"zh": "内容翻译"})
    TITLE_TRANSLATE = Column(Text, doc={"zh": "标题翻译"})
    NEWS_CODE = Column(String(40), doc={"zh": "文章唯一标识"})
    DATE = Column(Date, doc={"zh": "文章日期"})
    URL = Column(String(200), doc={"zh": "文章链接"})
    InsertTime = Column(DateTime, doc={"zh": "抓取时间"})
