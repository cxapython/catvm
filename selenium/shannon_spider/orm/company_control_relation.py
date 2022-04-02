# -*- encoding: utf-8 -*-

from sqlalchemy import Column, Date, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class  CompanyControlRelationItem(CommonFieldMixin, ItemBaseModel):
      """
      公司控股层级关系
      """
      __tablename__ = 'company_control_relation'
      desc = '公司控股层级关系'

      COMPANY_CODE = Column(VARCHAR(10), doc={'zh', '公司代码'})
      COMPANY_NAME = Column(VARCHAR(200), doc={'zh', '公司名称'})
      CONTROL_LEVEL = Column(VARCHAR(10), doc={'zh': '控制层级'})
      HOLD_COMPANY = Column(VARCHAR(200), doc={'zh': '持股公司'})
      HOLD_RATIO = Column(VARCHAR(10), doc={'zh': '持股比例'})
      HOLDED_COMPANY = Column(VARCHAR(200), doc={'zh': '被持股公司'})
