# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ImportantContractItem(CommonFieldMixin, ItemBaseModel):
    """重大合同字段定义"""

    __tablename__ = 'important_contract'

    desc = '重大合同数据'
    # 股票代码
    STOCK_CODE = Column(String(20), doc={'zh', '股票代码'})

    # 股票简称
    STOCK_SHORT = Column(String(20), doc={'zh', '股票简称'})

    # 公告日期
    NOTICE_DATE = Column(Date, doc={'zh', '公告日期'})

    # 合同类型
    CONTRACT_TYPE = Column(String(40), doc={'zh', '合同类型'})

    # 签署主体
    SIGN_MAIN = Column(String(40), doc={'zh', '签署主体'})

    # 其他签署方
    OTHER_SIGNER = Column(String(400), doc={'zh', '其他签署方'})

    # 与上市公司关系
    COMPANY_RELATION = Column(String(40), doc={'zh', '与上市公司关系'})

    # 合同金额
    CONTRACT_SUM = Column(Numeric(20, 3), doc={'zh', '合同金额'})

    # 上年度营业收入
    LAST_YEAR_INCOME = Column(Numeric(20, 3), doc={'zh', '上年度营业收入'})

    # 上年度营业收入的比例
    INCOME_RATIO = Column(Numeric(10, 3), doc={'zh', '上年度营业收入的比例'})

    # 合同名称
    CONTRACT_NAME = Column(String(400), doc={'zh', '合同名称'})

    # 爬取数据日期
    CREATED_AT = Column(Date, doc={'zh', '爬取数据日期'})







