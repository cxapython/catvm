from sqlalchemy import Column, Numeric, Integer,String
from shannon_spider.db import CommonFieldMixin, ItemBaseModel

class WorldBankNewItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'worldbank_country_new'

    desc = 'worldbank country excel 中数据 世界发展指标'

    COUNTRY_NAME = Column(String(50), index=True, doc={'zh': '国家及地区'})
    INDICATOR_TIME = Column(Integer, index=True, doc={'zh': '统计年份'})
    INDICATOR_CODE = Column(Integer, index=True, doc={'zh': '指标代码'})
    INDICATOR_VALUE = Column(Numeric(35, 15), doc={'zh': '指标数值'})
    INDICATOR_VALUE_YoY = Column(Numeric(35, 15), doc={'zh': '指标数值同比增长'})