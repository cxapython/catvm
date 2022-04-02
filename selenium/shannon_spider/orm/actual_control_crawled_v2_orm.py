# -*- encoding: utf-8 -*-
from sqlalchemy import Column, String, DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ControlCrawledV2Item(CommonFieldMixin, ItemBaseModel):
    '''控股信息'''
    __tablename__ = 'actual_control_crawled_v2'
    desc = '控股信息'
    S_INFO_WINDCODE = Column(String(40), doc={"zh": "公司代码"})
    COMPANY_NAME = Column(String(50), doc={"zh": "公司名字"})
    MARJOR_SHAREHOLDER = Column(String(100), doc={"zh": "控制股东"})
    MARJOR_SHAREHOLDER_RATIO = Column(String(200), doc={"zh": "控制股东持股比例"})
    ACTUAL_CONTROLLER = Column(String(100), doc={"zh": "实际控制人"})
    ACTUAL_CONTROLLER_RATIO = Column(String(200), doc={"zh": "实际控制人持股比例"})
    ULTIMATE_CONTROLLER = Column(String(100), doc={"zh": "最终控制人"})
    ULTIMATE_CONTROLLER_RATIO = Column(String(200), doc={"zh": "最终控制人持股比例"})
    UPGRADE_DATE = Column(DateTime,doc={'zh': '更新日期'})
