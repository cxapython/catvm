# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class NetValueOfWIPItem(CommonFieldMixin, ItemBaseModel):
    """每天的净值信息"""
    __tablename__ = 'net_value_of_WIP'

    registration_code = Column(VARCHAR(50), doc={'zh': '登记编码'})
    date = Column(DATETIME, doc={'zh': '日期'})
    product_net_value = Column(VARCHAR(50), doc={'zh': '产品净值'})
    cumulative_net_value = Column(VARCHAR(40), doc={'zh': '累计净值'})
    last_redemption_yield = Column(VARCHAR(40), doc={'zh': '最近一次兑付收益率'})
    start_date_of_business = Column(DATETIME, doc={'zh': "业务起始日"})
    end_date_of_business = Column(DATETIME, doc={'zh': "业务结束日"})
    product_status = Column(VARCHAR(200), doc={'zh': "产品状态"})
