# -*- encoding: utf-8 -*-
from sqlalchemy import Column, String, DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ControlLevelV2Item(CommonFieldMixin, ItemBaseModel):
    '''实际控制人控制路径'''
    __tablename__ = 'control_relation_crawled_v2'
    desc = '实际控制人控制路径'
    S_INFO_WINDCODE = Column(String(40), doc={"zh": "公司代码"})
    COMPANY_NAME = Column(String(50), doc={"zh": "公司名字"})
    LEVEL = Column(String(20), doc={"zh": "层级"})
    HOLD_COMPANY = Column(String(200), doc={"zh": "持股方"})
    HOLD_RATIO = Column(String(200), doc={"zh": "持股比例"})
    HOLDED_COMPANY = Column(String(100), doc={"zh": "被持股方"})
    UPGRADE_DATE = Column(DateTime, doc={'zh': '更新日期'})
