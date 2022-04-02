from sqlalchemy import Column, VARCHAR, Numeric, DATE, BIGINT, INT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class TopTenShareholdersListItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'top_ten_shareholders_list'
    desc='前十大股东（东方财富）'

    S_HOLDER_NAME = Column(VARCHAR(100), doc={'zh': '股东名称'})
    S_RANK = Column(INT(), doc={'zh': '股东排名'})
    S_CODE = Column(VARCHAR(100), doc={'zh': '股票代码'})
    S_NAME = Column(VARCHAR(100), doc={'zh': '股票简称'})
    R_DATE = Column(DATE, doc={'zh': '报告期'})
    S_AMOUNT = Column(Numeric(15, 1), doc={'zh': '数量'})
    S_TOTAL_VALUE = Column(Numeric(15, 2), doc={'zh': '流通市值'})
    ANNOUNCEMENT_DATE = Column(DATE, doc={'zh': '公告日'})
    S_RATIO = Column(VARCHAR(50), doc={'zh': '持股占总股比'})
    ASSUM_TOTAL = Column(BIGINT(), doc={'zh': '推断总股本 ASSUM_TOTAL= SHAREHDNUM/SHAREHDRATIO 推断总股本为整数（向上）'})