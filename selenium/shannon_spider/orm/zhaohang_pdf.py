# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: zhaohang_pdf.py
@time: 2018/11/12 17:50
"""
from sqlalchemy import Column, String
from shannon_spider.db import  ItemBaseModel, CommonFieldMixin

class ZhaoHangPdfItem(CommonFieldMixin, ItemBaseModel):
    ''' 货币网PDF下载结果'''
    __tablename__ = 'zhaohang_pdf'
    desc = '企业债信息'
    # ID = Column(Integer, primary_key=True)
    BONDNAME = Column(String(50), doc={"zh": "债券简称"})
    BONDCODE = Column(String(50), doc={"zh": "债券代码"})
    BONDFULLNAME = Column(String(150), doc={"zh": "债券全称"})
    ISINCODE = Column(String(40), doc={"zh": "ISIN码"})
    ENTYFULLNAME = Column(String(100), doc={"zh": "发行人"})
    BONDTYPE = Column(String(50), doc={"zh": "债券类型"})
    BONDCCY = Column(String(40), doc={"zh": "币种"})
    ISSUE_DATE = Column(String(40), doc={"zh": "债券发行日"})
    MRTY_DATE = Column(String(40), doc={"zh": "到期兑付日"})
    LSTNG_DATE = Column(String(40), doc={"zh": "上市交易日"})
    DLSTNG_DATE = Column(String(40), doc={"zh": "债券摘牌日"})
    BOND_PERIOD = Column(String(40), doc={"zh": "债券期限"})
    PAR_VALUE = Column(String(40), doc={"zh": "面值(元)"})
    ISSUE_PRICE = Column(String(40), doc={"zh": "发行价格(元)"})
    PLND_ISSUE_AMNT = Column(String(40), doc={"zh": "计划发行量(亿)"})
    ISSUE_AMNT = Column(String(40), doc={"zh": "实际发行量(亿)"})
    INTRST_BSS = Column(String(50), doc={"zh": "计息基础"})
    COUPON_TYPE = Column(String(50), doc={"zh": "息票类型"})
    FIRST_VALUE_DATE = Column(String(40), doc={"zh": "债券起息日"})
    COUPON_FRQNCY = Column(String(40), doc={"zh": "付息频率"})
    PAR_COUPON_RATE = Column(String(40), doc={"zh": "票面利率(%)"})
    ISYLDRATE = Column(String(40), doc={"zh": "发行收益率(%)"})
    REFYLD = Column(String(40), doc={"zh": "参考收益率(%)"})
    BNCH_MK_RATE_NM = Column(String(40), doc={"zh": "基准利率名"})
    BNCH_MK_RATE = Column(String(40), doc={"zh": "基准利率"})
    BNCH_SPREAD_RATE = Column(String(40), doc={"zh": "基准利差(%)"})
    CIRCU_AREA = Column(String(40), doc={"zh": "流通范围"})
    CREDIT_RATE_ENTY = Column(String(400), doc={"zh": "信用评级机构"})     #
    EXERCISE_INFO = Column(String(500), doc={"zh": "行权类型"})         #
    CUSTODIAN = Column(String(100), doc={"zh": "托管机构"})
    PLTFRMINDCTR = Column(String(200), doc={"zh": "适用市场"})
    DETAIL_PAGE_URL = Column(String(80),doc={"zh":"详细页的链接"})
    ANNOUNCEMENT_INFO = Column(String(10000), doc={"zh": "公报信息"})    #
    ANNOUNCEMENT_CODE = Column(String(10),doc={"zh":'公告分类编码'})
    BONDDEFINEDCODE = Column(String(50),doc={"zh":"债券标识码"})

    KEYWORD = Column(String(30),doc={"zh":'公告标题包含的关键字'})
    PDF_URL = Column(String(500),doc={"zh":"PDF链接"})
    PDF_TITLE = Column(String(200),doc={"zh":"PDF标题"})
    # ANNOUNCEMENT_TYPE = Column(String(50),doc={"zh":"公告类型"})
    # ANNOUNCEMENT_DATE = Column(String(50),doc={"zh":"公告日期"})
    FILEPATH = Column(String(200),doc={"zh":"文件路径"})
    FILENAME = Column(String(200), doc={"zh": "文件名"})