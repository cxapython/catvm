# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN, TEXT, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class GeLongHuiItem(CommonFieldMixin, ItemBaseModel):
    """格隆汇"""

    __tablename__ = 'daily_issue_gelonghui'

    desc = '每日重要事件'

    # 标题
    TITLE = Column(String(100), doc={'zh', '标题'})

    # 日期
    DATE = Column(String(20), doc={'zh', '日期'})

    # 格隆汇
    SOURCE = Column(String(10), doc={'zh', '格隆汇'})

    # 主体页面
    CONTENT = Column(TEXT, doc={'zh', '主体页面'})

    # 链接
    URL = Column(String(100), doc={'zh', '链接'})

