from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class Hs300ComponentItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'hs300_component'

    desc = '沪深300股票池爬取'

    SEC_CODE = Column(VARCHAR(50), doc={'zh': '品种代码'})
    SEC_NAME = Column(VARCHAR(50), doc={'zh': '品种名称'})
    RECRUIT_DATE = Column(VARCHAR(50), doc={'zh': '纳入日期'})
    DATE = Column(VARCHAR(50), doc={'zh': '运行日期'})