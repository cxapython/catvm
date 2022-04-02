# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN, TEXT
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ApprovalOfBloodProductVaccineItem(CommonFieldMixin, ItemBaseModel):
    """"""

    __tablename__ = 'approval_of_blood_product_vaccine'

    desc = '血制品疫苗批签发数据库'
    # 产品名称
    DRUG_NAME = Column(String(200), doc={'zh', '产品名称'})

    # 规格
    SPECIFICATION = Column(TEXT, doc={'zh', '规格'})

    # 批号
    BATCH = Column(String(20), doc={'zh', '批号'})

    # 签发量
    ISSUE_AMOUNT = Column(String(50), doc={'zh', '签发量'})

    # 有效期至
    VALID_UNTIL = Column(String(50), doc={'zh', '有效期至'})

    # 生产企业
    DRUG_COMPANY = Column(String(150), doc={'zh', '生产企业'})

    # 收检编号
    INSPECTION_NUMBER = Column(String(50), doc={'zh', '收检编号'})

    # 证书编号
    CERTIFICATE_NUMBER = Column(String(50), doc={'zh', '证书编号'})

    # 报告编号
    REPORT_NUMBER = Column(String(50), doc={'zh', '报告编号'})

    # 签发日期
    ISSUE_DATE = Column(Date, doc={'zh', '签发日期'})

    # 签发结论
    ISSUE_CONCLUSION = Column(String(100), doc={'zh', '签发结论'})

    # 签发机构
    SIGNING_AUTHORITIES = Column(String(100), doc={'zh', '签发机构'})

    # 标题
    TITLE = Column(String(100), doc={'zh', '标题'})


