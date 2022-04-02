# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CarSalesItem(CommonFieldMixin, ItemBaseModel):
    """数据局字段"""

    __tablename__ = 'car_sales_crawled'

    desc = '汽车销量'
    # 类别
    CAR_CATEGORY = Column(String(60), doc={'zh': '类别'})

    # 销量排名时间
    SALES_TIME = Column(Date, doc={'zh': '销量排名时间'})

    # 销量排名
    SALES_RANK = Column(Integer, doc={'zh': '销量排名'})

    # 车型
    CAR_TYPE = Column(String(60), doc={'zh': '车型'})

    # 厂商
    CAR_MANUFACTURER = Column(String(60), doc={'zh': '厂商'})

    # 当月销量
    CAR_SALES = Column(Integer, doc={'zh': '当月销量'})

    # 当年截止当月累计销量
    CAR_SALES_TOTAL = Column(Integer, doc={'zh': '当年截止当月累计销量'})

    # 销量数据来源url
    SALES_SOURCE = Column(Integer, doc={'zh': '销量数据来源url'})

