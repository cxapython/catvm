# encoding: utf-8
'''
@author: zhao zhibo
@file: AShare_BShare_orm.py
@time: 2021/1/14 上午10:51
@desc:
'''
from sqlalchemy import Column, VARCHAR, Numeric, Date, Time, Integer,Text
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class AShareBShareOrm(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'AShare_BShare'

    S_INFO_CODE = Column(VARCHAR(20), doc={'zh':'A股代码'})
    BShare_CODE = Column(VARCHAR(20), doc={'zh':'B股代码'})
    BShare_SName = Column(VARCHAR(20), doc={'zh':'B股简称'})
    create_date = Column(Date)