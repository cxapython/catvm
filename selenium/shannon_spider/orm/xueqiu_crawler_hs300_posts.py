from sqlalchemy import Column, VARCHAR, TEXT, DATETIME, INT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class XueqiuCrawlerHs300PostsItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'xueqiu_crawler_hs300_posts'

    desc = '沪深300股票池雪球数据爬取'

    SEC_CODE = Column(VARCHAR(50), doc={'zh': '股票代码,代码后缀市场简称'})
    SEC_NAME = Column(VARCHAR(50), doc={'zh': '股票简称'})
    CONTENT = Column(TEXT, doc={'zh': '贴子内容'})
    CONTENT_TYPE = Column(VARCHAR(100), doc={'zh': '贴子类型'})
    POST_TITLE = Column(VARCHAR(500), doc={'zh': '帖子标题, 短评论没有标题'})
    POST_URL = Column(VARCHAR(200), doc={'zh': '帖子URL'})
    POST_PAGE_URL = Column(VARCHAR(200), doc={'zh': '评论页面URL'})
    POST_TIME = Column(DATETIME, doc={'zh': '贴子发布时间'})
    POSTER = Column(VARCHAR(50), doc={'zh': '贴子发布者'})
    POST_ID = Column(VARCHAR(100), index=True, doc={'zh': '帖子ID'})