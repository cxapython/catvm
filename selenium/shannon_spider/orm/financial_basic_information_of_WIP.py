# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class BasicInformationOfWIPItem(CommonFieldMixin, ItemBaseModel):
    """基础理财产品信息"""
    __tablename__ = 'basic_information_of_WIP'

    product_name = Column(VARCHAR(200), doc={'zh': "产品名称"})
    registration_code = Column(VARCHAR(200), doc={'zh': "登记编码"})
    issuer = Column(VARCHAR(200), doc={'zh': "发行机构"})
    operation_mode = Column(VARCHAR(200), doc={'zh': "运作模式"})
    recruitment_method = Column(VARCHAR(200), doc={'zh': "募集方式"})
    term_type = Column(VARCHAR(200), doc={'zh': "期限类型	"})
    currency = Column(VARCHAR(200), doc={'zh': "募集币种"})
    investment_nature = Column(VARCHAR(200), doc={'zh': "投资性质"})
    risk_rate = Column(VARCHAR(200), doc={'zh': "风险等级"})
    start_date_of_recruitment = Column(DATETIME, doc={'zh': "募集起始日期"})
    end_date_of_recruitment = Column(DATETIME, doc={'zh': "募集结束日期"})
    start_date_of_product = Column(DATETIME, doc={'zh': "产品起始日期"})
    end_date_of_product = Column(DATETIME, doc={'zh': "产品结束日期"})
    actual_days = Column(VARCHAR(200), doc={'zh': "实际天数"})
    performance_benchmark = Column(VARCHAR(200), doc={'zh': "业绩比较基准"})
    initial_net_value = Column(VARCHAR(200), doc={'zh': "初始净值"})
    income_type = Column(VARCHAR(200), doc={'zh': "收益类型"})
    investment_asset_type = Column(VARCHAR(200), doc={'zh': "投资资产类型"})
    expected_minimum_yield = Column(VARCHAR(200), doc={'zh': "预期最低收益率"})
    expected_maximum_yield = Column(VARCHAR(200), doc={'zh': "预期最高收益率"})
    sales_region = Column(VARCHAR(200), doc={'zh': "销售区域"})
