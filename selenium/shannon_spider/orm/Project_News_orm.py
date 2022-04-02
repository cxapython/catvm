# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ProjectNewsItem(CommonFieldMixin, ItemBaseModel):
    """
     上交所科创板项目动态
     """
    __tablename__ = 'Project_News'
    desc = '上交所科创板项目动态'
    ISSUER_NAME = Column(VARCHAR(100), doc={'zh', '发行人全称'})
    CHECK_STATUS = Column(VARCHAR(100), doc={'zh', '审核状态'})
    REGISTER_LOCATION = Column(VARCHAR(100), doc={'zh', '注册地'})
    CSRC_INDUSTRY = Column(VARCHAR(200), doc={'zh', '证监会行业'})
    SPONSOR_NAME = Column(VARCHAR(200), doc={'zh', '保荐机构'})
    LAW_OFFICE = Column(VARCHAR(200), doc={'zh', '律师事务所'})
    ACCOUNTING_FIRM = Column(VARCHAR(200), doc={'zh', '会计师事务所'})
    DATE_LAST_UPDATED = Column(VARCHAR(100), doc={'zh', '更新日期'})
    DATE_ACCEPTED = Column(VARCHAR(100), doc={'zh', '受理日期'})
