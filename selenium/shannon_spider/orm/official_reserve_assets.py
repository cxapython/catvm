# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class OfficialReserveAssetsItem(CommonFieldMixin, ItemBaseModel):
    """
    官方储备资产
    """
    __tablename__ = 'official_reserve_assets'
    desc = '官方储备资产'
    
    ITEM = Column(VARCHAR(50), doc={'zh', '指标'})
    TIME = Column(VARCHAR(10), doc={'zh', '时间'})
    VALUE = Column(DECIMAL(10,2), doc={'zh', '数值'}) # DECIMAL 第一个参数代表10进制，第二参数代表保留2位小数
    UNIT_OF_MEASUREMENT = Column(VARCHAR(20), doc={'zh', '单位'})
    LEVEL = Column(Integer, doc={'zh', '等级'})
