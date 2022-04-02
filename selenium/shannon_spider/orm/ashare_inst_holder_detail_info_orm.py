# coding=utf-8
from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class AshareInstHolderDetailInfoItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'ashare_inst_holder_detail_info'

    desc = '上市公司机构股东信息'

    s_info_windcode = Column(VARCHAR(50), doc={'zh': 'WIND代码'})
    report_period = Column(DATETIME, doc={'zh': '报告期'})
    s_holder_sname = Column(VARCHAR(50), doc={'zh': '机构简称'})
    s_holder_code = Column(VARCHAR(50), doc={'zh': '机构代码'})
    s_holder_category = Column(VARCHAR(50), doc={'zh': '机构属性'})
    s_holder_quantity = Column(VARCHAR(50), doc={'zh': '持股总数'})
    market_value_of_shareholding = Column(VARCHAR(50), doc={'zh': '持股市值'})
    s_holder_pct_of_total_share = Column(VARCHAR(50), doc={'zh': '占总股本比例'})
    s_holder_pct_of_outstanding_share = Column(VARCHAR(50), doc={'zh': '占流通股比例'})
