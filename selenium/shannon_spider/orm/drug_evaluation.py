# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class DrugEvaluationItem(CommonFieldMixin, ItemBaseModel):
    """国家食品药品监督管理总局药品审评中心"""

    __tablename__ = 'cde_drug_review_catalogue'

    desc = '受理品种目录'
    # 受理号
    DRUG_ID = Column(String(40), doc={'zh', '受理号'})

    # 药品名称
    DRUG_NAME = Column(String(100), doc={'zh', '药品名称'})

    # 药品类型
    DRUG_CATEGORY = Column(String(50), doc={'zh', '药品类型'})

    # 申请类型
    APPLICATION_TYPE = Column(String(20), doc={'zh', '申请类型'})

    # 注册分类
    REGISTRY_CLASSIFICATION = Column(String(20), doc={'zh', '注册分类'})

    # 企业名称
    DRUG_COMPANY = Column(String(200), doc={'zh', '企业名称'})

    # 承办日期
    RECEPTION_DATE = Column(Date, doc={'zh', '承办日期'})

    # 收审情况
    APPLICATION_PROCESSING = Column(String(20), doc={'zh', '收审情况'})


