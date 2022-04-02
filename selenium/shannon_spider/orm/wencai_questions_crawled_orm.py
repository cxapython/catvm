from sqlalchemy import Column, String, TEXT, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class WencaiQuestions(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'wencai_questions_crawled'

    desc = '同花顺i问财问答'

    ISSUER = Column(String(50), doc={'zh': '提问者'})
    QUESTION = Column(TEXT, doc={'zh': '问题'})
    QUESTION_TIME = Column(DATETIME, doc={'zh': '问题时间'})
    REPLY = Column(TEXT, doc={'zh': '回答'})
    REPLY_TIME = Column(DATETIME, doc={'zh': '回答时间'})
