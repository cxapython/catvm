# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATE
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SsePrivateChangedItem(CommonFieldMixin, ItemBaseModel):
    '''上交所募集债券信息'''
    __tablename__ = 'sse_private_changed'
    desc = '上交所募集债券信息'

    bond_name = Column(VARCHAR(1000), doc={'zh': '债券名称'})
    issuer = Column(VARCHAR(500), doc={'zh': '发行人'})
    underwriter = Column(VARCHAR(500), doc={'zh': '承销商/管理人'})
    category = Column(VARCHAR(100), doc={'zh': '债券类别'})
    issue_money = Column(VARCHAR(100), doc={'zh': '拟发行金额(亿元)'})
    status = Column(VARCHAR(100), doc={'zh': '项目状态'})
    update_date = Column(DATE, doc={'zh': '更新日期'})
    accept_date = Column(DATE, doc={'zh': '受理日期'})
