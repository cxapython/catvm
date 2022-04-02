# codig=utf-8

from sqlalchemy import Column, VARCHAR, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class StockExchangeItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'stock_exchange_Inquiry_letter'

    desc = '深交所、上交所 监管问询函件'

    CODE = Column(VARCHAR(20), doc={'zh': '公司代码'})
    NAME = Column(VARCHAR(100), doc={'zh': '公司简称'})
    DATE = Column(DATE, doc={'zh': '发函日期'})
    TYPE = Column(VARCHAR(100), doc={'zh': '函件类别'})
    TITLE = Column(VARCHAR(200), doc={'zh': '标题'})
    URL = Column(VARCHAR(200), doc={'zh': '文档链接'})
    PDF_URL = Column(VARCHAR(200), doc={'zh': '存储路径'})
    MARKET = Column(VARCHAR(50), doc={'zh': '上交所or深交所'})