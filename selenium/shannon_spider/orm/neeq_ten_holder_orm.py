# coding=utf-8

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class NeeqTenHolderItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'neeq_ten_holder'

    desc = '十大股东数据'

    STOCK_CODE = Column(VARCHAR(100), doc={'zh', '公司代码'})
    SHORT_NAME = Column(VARCHAR(100), doc={'zh': '公司简称'})
    END_DATE = Column(DATETIME, doc={'zh': '截止日期'})
    HOLDER_NAME = Column(VARCHAR(200), doc={'zh': '股东名称'})
    STOCK_AMOUNT = Column(VARCHAR(200), doc={'zh': '持股数'})
    HOLD_RATIO = Column(VARCHAR(200), doc={'zh': '持股比例'})




