from sqlalchemy import Column, VARCHAR, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class DailyIssueHuaerjiejianwenItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'daily_issue_huaerjiejianwen'
    desc = '华尔街见闻'

    TITLE = Column(VARCHAR(200), doc={'zh': '标题'})
    DATE = Column(VARCHAR(50), doc={'zh': '日期'})
    CONTENT = Column(TEXT, doc={'zh': '页面内容'})
    SOURCE = Column(VARCHAR(200), doc={'zh': '华尔街见闻'})
    URL = Column(VARCHAR(1000), doc={'zh': '链接'})