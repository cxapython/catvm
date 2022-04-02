from sqlalchemy import Column, VARCHAR, TEXT, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class XueqiuCrawlerHs300CommentItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'xueqiu_crawler_hs300_comment'

    desc = '沪深300股票池雪球数据爬取'

    POST_ID = Column(VARCHAR(100), index=True, doc={'zh': '贴子ID'})
    SEC_FOLLOWERS = Column(VARCHAR(50), doc={'zh': '股票每日关注人数'})
    COMMENTER = Column(VARCHAR(50), doc={'zh': '评论人'})
    COMMENT_TIME = Column(DATETIME, index=True, doc={'zh': '评论时间'})
    COMMENT_TO = Column(VARCHAR(100), doc={'zh': '评论回复对象'})
    COMMENT_CONTENT = Column(TEXT, doc={'zh': '评论内容  表情解析为文字'})
    COMMENTER_FANS = Column(VARCHAR(50), doc={'zh': '评论人粉丝数'})
    COMMENTER_FALLOWS = Column(VARCHAR(50), doc={'zh': '评论人关注数'})

    POSTER_FANS = Column(VARCHAR(50), doc={'zh': '发布者粉丝数'})
    POSTER_FOLLOWS = Column(VARCHAR(50), doc={'zh': '发布者关注数'})
    POST_RETWEET = Column(VARCHAR(50), doc={'zh': '帖子的转发数'})
    POST_LIKES = Column(VARCHAR(50), doc={'zh': '帖子的点赞数'})