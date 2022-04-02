# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATE, DECIMAL
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class CapitalFlowItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'capital_flow'
    desc = '资金流向'
    
    STOCK_CODE = Column(VARCHAR(10), doc={'zh', '股票代码'})      
    DATE = Column(DATE, doc={'zh', '日期'})
    CLOSING_PRICE = Column(DECIMAL(10,2), doc={'zh', '收盘价'})
    MAIN_NET_INFLOW = Column(VARCHAR(20), doc={'zh', '主力净流入额'})
    MAIN_NET_INFLOW_RATIO = Column(VARCHAR(20), doc={'zh', '主力净流入占比'})
    SUPER_NET_INFLOW = Column(VARCHAR(20), doc={'zh', '超大单净流入额'})
    SUPER_NET_INFLOW_RATIO = Column(VARCHAR(20), doc={'zh', '超大单净流入占比'})
    LARGE_NET_INFLOW = Column(VARCHAR(20), doc={'zh', '大单净流入额'})
    LARGE_NET_INFLOW_RATIO = Column(VARCHAR(20), doc={'zh', '大单净流入占比'})
    MIDDLE_NET_INFLOW = Column(VARCHAR(20), doc={'zh', '中单净流入额'})
    MIDDLE_NET_INFLOW_RATIO = Column(VARCHAR(20), doc={'zh', '中单净流入占比'})
    SMALL_NET_INFLOW = Column(VARCHAR(20), doc={'zh', '小单净流入额'})
    SMALL_NET_INFLOW_RATIO = Column(VARCHAR(20), doc={'zh', '小单净流入占比'})
