# codig=utf-8

from sqlalchemy import Column, VARCHAR, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class StockExchangePunishItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'stock_exchange_punishment_letter'

    desc = '上交所、深交所 监管处罚措施'

    CODE = Column(VARCHAR(20), doc={'zh': '证券代码'})
    NAME = Column(VARCHAR(100), doc={'zh': '证券简称'})
    DATE = Column(DATE, doc={'zh': '发函日期'})
    TYPE = Column(VARCHAR(100), doc={'zh': '函件类别'})
    TITLE = Column(VARCHAR(200), doc={'zh': '标题'})
    URL = Column(VARCHAR(200), doc={'zh': '文档链接'})
    PDF_URL = Column(VARCHAR(200), doc={'zh': '存储路径'})
    MARKET = Column(VARCHAR(50), doc={'zh': '上交所or深交所'})
    RELATED_PARTY = Column(VARCHAR(200), doc={'zh': '涉及对象'})