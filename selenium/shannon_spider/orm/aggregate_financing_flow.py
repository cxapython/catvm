# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class AggregateFinancingFlowItem(CommonFieldMixin, ItemBaseModel):
    """
    社会融资规模增量统计
    """
    __tablename__ = 'aggregate_financing_to_the_real_economy_flow'
    desc = '社会融资规模增量统计'
    
    ITEM = Column(VARCHAR(100), doc={'zh', '项目'})
    TIME = Column(VARCHAR(10), doc={'zh', '时间'})
    VALUE = Column(DECIMAL, doc={'zh', '数值'}) # DECIMAL 第一个参数代表10进制，第二参数代表保留2位小数
    UNIT_OF_MEASUREMENT = Column(VARCHAR(20), doc={'zh', '单位'})
    LEVEL = Column(Integer, doc={'zh', '等级'})
