from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class GelongHuiSubjectItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'gelonghui_subject'

    SUBJECT = Column(VARCHAR(50), doc={'zh': '主题名称'})
    SUBJECT_URL = Column(VARCHAR(500), doc={'zh': '主题url'})
    NEXT_TITLE = Column(VARCHAR(100), doc={'zh': '主题分类下小标题'})
    DATE = Column(VARCHAR(50), doc={'zh': '小标题时间'})
    NEXT_TITLE_URL = Column(VARCHAR(500), doc={'zh': '主题分类下小标题url'})