# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATE, DECIMAL
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class SHStockExchangeItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'shanghai_stock_exchange'
    desc = '上海证券交易所'
    
    BOND_CODE = Column(VARCHAR(10), doc={'zh', '债券代码'})
    BOND_ABBR = Column(VARCHAR(50), doc={'zh', '债券简称'})
    ISSUE_OWNER = Column(VARCHAR(50), doc={'zh', '发行人'})
    BOND_FULL = Column(VARCHAR(100), doc={'zh', '债券全称'})
    BOND_TYPE = Column(VARCHAR(20), doc={'zh', '债券类型'})
    ISSUE_VALUE = Column(DECIMAL(10,4), doc={'zh', '发行量(亿元)'})
    SSE_TOTAL_AMT = Column(DECIMAL(10,4), doc={'zh', '上交所上市总量(亿元)'})
    ISSUED_START_DAY = Column(DATE, doc={'zh', '发行起始日'})
    ISSUED_END_DAY = Column(DATE, doc={'zh', '发行终止日'})
    START_DATE = Column(DATE, doc={'zh', '起息日期'})
    END_DATE = Column(DATE, doc={'zh', '到期日期'})
    LISTING_DATE = Column(DATE, doc={'zh', '上市日期'})
    BANK_CODE = Column(VARCHAR(10), doc={'zh', '银行间代码'})
    INTEREST_TYPE = Column(VARCHAR(20), doc={'zh', '计息方式'})
    PAY_TYPE = Column(VARCHAR(20), doc={'zh', '付息方式'})
    FACE_RATE = Column(DECIMAL(10,2), doc={'zh', '票面利率(%)'})
    TERM_YEAR = Column(VARCHAR(10), doc={'zh', '债券期限(年)'})
    BASE_RATE = Column(VARCHAR(10), doc={'zh', '基准利率(%)'})
    FLOAT_SPREAD = Column(VARCHAR(10), doc={'zh', '浮动利差(%)'})
    RATE = Column(VARCHAR(10), doc={'zh', '标准折算率'})
    CLEAN_PRICE = Column(VARCHAR(20), doc={'zh', '债券估值'})
    MANAGE_TYPE = Column(VARCHAR(20), doc={'zh', '投资者适当性管理'})
    TRADE_TYPE = Column(VARCHAR(30), doc={'zh', '交易方式'})
    BOND_RATING = Column(VARCHAR(10), doc={'zh', '债券评级'})
    MAIN_RATING = Column(VARCHAR(10), doc={'zh', '主体评级'})
    REPORT_TITLE = Column(VARCHAR(2000), doc={'zh', '公告名称'})
    REPORT_URL = Column(VARCHAR(2000), doc={'zh', '公告链接'})
    REPORT_DATE = Column(VARCHAR(1000), doc={'zh', '公告日期'})
