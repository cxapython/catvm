# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, Date
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class  CompanyHolderItem(CommonFieldMixin, ItemBaseModel):
	"""
	公司股东、实际控制人、最终控制人抓取结果
	"""
	__tablename__ = 'company_holder'

	desc = '公司股东、实际控制人、最终控制人'

	COMPANY_CODE = Column(VARCHAR(10), doc={'zh', '公司WIND码'})
	COMPANY_NAME = Column(VARCHAR(200), doc={'zh', '公司名称'})
	MAJOR_SHAREHOLDER = Column(VARCHAR(200), doc={'zh': '控制股东'})
	MAJOR_SHAREHOLDER_RATIO = Column(VARCHAR(200), doc={'zh': '控制股东持股比例'})
	ACTUAL_SHAREHOLDER = Column(VARCHAR(200), doc={'zh': '实际控制股东'})
	ACTUAL_SHAREHOLDER_RATIO = Column(VARCHAR(200), doc={'zh': '实际控制股东持股比例'})
	ULTIMATE_SHAREHOLDER = Column(VARCHAR(200), doc={'zh': '最终控制股东'})
	ULTIMATE_SHAREHOLDER_RATIO = Column(VARCHAR(200), doc={'zh': '最终控制股东持股比例'})
	
