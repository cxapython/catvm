# coding=utf-8

from sqlalchemy import Column, VARCHAR, INTEGER, TIMESTAMP, text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class NeeqCompListItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'neeq_comp_list_new'

    desc = '新三板公司名录数据'

    STOCK_CODE = Column(VARCHAR(100), index=True, doc={'zh', '公司代码'})
    SHORT_NAME = Column(VARCHAR(100), doc={'zh': '公司简称'})
    EXCHANGE_TYPE = Column(VARCHAR(100), doc={'zh': '交易方式'})
    INDUSTRY = Column(VARCHAR(200), doc={'zh': '所属行业'})
    SECURITY = Column(VARCHAR(200), doc={'zh': '主办券商'})
    REGION = Column(VARCHAR(100), doc={'zh': '地区'})
    FULL_NAME = Column(VARCHAR(200), doc={'zh': '公司全称'})
    VALID = Column(INTEGER, doc={'zh': '是否为有效数据'})
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'), doc={'zh': '记录创建时间'})
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'), doc={'zh': '更新时间'})
