# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: ccs_cashflow_statement.py
@time: 2018/10/20 11:15

中概股
"""
from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsCashflowStatementItem(CommonFieldMixin, ItemBaseModel):
    '''东方财富对中概股现金流量表抓取结果'''
    __tablename__ = 'ccs_cashflow_statement'
    desc = '中概股现金流量表数据'
    CODE = Column(String(40), doc={'zh': '股票代码'})
    NAME = Column(String(40), doc={'zh': '股票名称'})
    BBJZR = Column(String(40), doc={'zh': '日期'})
    CBLX = Column(String(40), doc={'zh': '财报类型'})
    NJR = Column(String(40), doc={'zh': '年结日'})
    BZ = Column(String(40), doc={'zh': '币种'})
    JYYWTZ = Column(String(40), doc={'zh': '经营业务调整'})
    JLR = Column(String(40), doc={'zh': '净利润'})
    ZJJTX = Column(String(40), doc={'zh': '折旧及摊销'})
    JYGPDBCK = Column(String(40), doc={'zh': '基于股票的补偿费'})
    JZJBB = Column(String(40), doc={'zh': '减值及拨备'})
    DYSDS = Column(String(40), doc={'zh': '递延所得税'})
    ZCCZSY = Column(String(40), doc={'zh': '资产处置损益'})
    TZSY = Column(String(40), doc={'zh': '投资损益'})
    CGYY = Column(String(40), doc={'zh': '重估盈余'})
    HDSS = Column(String(40), doc={'zh': '汇兑损益'})
    YLJTXFL = Column(String(40), doc={'zh': '养老及退休福利'})
    QYXTZSY = Column(String(40), doc={'zh': '权益性投资损益'})
    WMQBFCB = Column(String(40), doc={'zh': '未满期保费储备'})
    ZBXKTHFBPK = Column(String(40), doc={'zh': '再保险可摊回分保赔款'})
    CYDSDK = Column(String(40), doc={'zh': '持有待售贷款'})
    JYYWTZQTXM = Column(String(40), doc={'zh': '经营业务调整其他项目'})
    JYYWTZHJX = Column(String(40), doc={'zh': '经营业务调整合计项'})
    JYYW = Column(String(40), doc={'zh': '经营业务'})
    YSZKJPJ = Column(String(40), doc={'zh': '应收账款及票据'})
    CH = Column(String(40), doc={'zh': '存货'})
    YFKXJQTYSK = Column(String(40), doc={'zh': '预付款项及其他应收款'})
    DTFYJQTZC = Column(String(40), doc={'zh': '待摊费用及其他资产'})
    YSGLFKX = Column(String(40), doc={'zh': '应收关联方款项'})
    YFGLFKX = Column(String(40), doc={'zh': '应付关联方款项'})
    YFZKJPJ = Column(String(40), doc={'zh': '应付账款及票据'})
    YSKXJQTYFK = Column(String(40), doc={'zh': '预收款项及其他应付款'})
    DYSR = Column(String(40), doc={'zh': '递延收入'})
    YFSX = Column(String(40), doc={'zh': '应付税项'})
    YTFYJQTFZ = Column(String(40), doc={'zh': '预提费用及其他负债'})
    CKJXZXXJ = Column(String(40), doc={'zh': '存款及限制性现金'})
    YSLX = Column(String(40), doc={'zh': '应收利息'})
    YFLX = Column(String(40), doc={'zh': '应付利息'})
    QTJYHDCSDXJLLZE = Column(String(40), doc={'zh': '其他经营活动产生的现金流量总额'})
    JYYWJQTXM = Column(String(40), doc={'zh': '经营业务其他项目'})
    JYHDCSDXJLLJE = Column(String(40), doc={'zh': '经营活动产生的现金流量净额'})
    TZYW = Column(String(40), doc={'zh': '投资业务'})
    CKZJJS = Column(String(40), doc={'zh': '存款增加(减少)'})
    GMGDZC = Column(String(40), doc={'zh': '购买固定资产'})
    CZGDZC = Column(String(40), doc={'zh': '处置固定资产'})
    GJWXZCJQTZC = Column(String(40), doc={'zh': '购建无形资产及其他资产'})
    CZWXZCJQTZC = Column(String(40), doc={'zh': '处置无形资产及其他资产'})
    TZZFXJ = Column(String(40), doc={'zh': '投资支付现金'})
    ZWCH = Column(String(40), doc={'zh': '债务偿还'})
    CSFSGS = Column(String(40), doc={'zh': '出售附属公司'})
    SGFSGS = Column(String(40), doc={'zh': '收购附属公司'})
    QTTZHDCSDXJLLJE = Column(String(40), doc={'zh': '其他投资活动产生的现金流量净额'})
    TZYWQTXM = Column(String(40), doc={'zh': '投资业务其他项目'})
    TZHDCSDXJLLJE = Column(String(40), doc={'zh': '投资活动产生的现金流量净额'})
    CZYW = Column(String(40), doc={'zh': '筹资业务'})
    FXGF = Column(String(40), doc={'zh': '发行股份'})
    HGGF = Column(String(40), doc={'zh': '回购股份'})
    FXZQ = Column(String(40), doc={'zh': '发行债券'})
    SHZQ = Column(String(40), doc={'zh': '赎回债券'})
    GXZF = Column(String(40), doc={'zh': '股息支付'})
    XSGPQQSD = Column(String(40), doc={'zh': '行使股票期权所得'})
    XZJK = Column(String(40), doc={'zh': '新增借款'})
    XJJQYZJJS = Column(String(40), doc={'zh': '现金及权益增加(减少)'})
    DKZJJS = Column(String(40), doc={'zh': '垫款增加(减少)'})
    CHJK = Column(String(40), doc={'zh': '偿还借款'})
    DKSY = Column(String(40), doc={'zh': '贷款收益'})
    FXFYXG = Column(String(40), doc={'zh': '发行费用相关'})
    PJXGSY = Column(String(40), doc={'zh': '票据相关收益'})
    CKJXZXXJZJJS = Column(String(40), doc={'zh': '存款及限制性现金增加(减少)'})
    CESSYH = Column(String(40), doc={'zh': '超额税收优惠'})
    QTCZHDCSDXJLLJE = Column(String(40), doc={'zh': '其他筹资活动产生的现金流量净额'})
    CZYWQTXM = Column(String(40), doc={'zh': '筹资业务其他项目'})
    CZHDCSDXJLLJE = Column(String(40), doc={'zh': '筹资活动产生的现金流量净额'})
    HLBDYX = Column(String(40), doc={'zh': '汇率变动影响'})
    XJJXJDJWZJJSE = Column(String(40), doc={'zh': '现金及现金等价物增加(减少)额'})
    XJJXJDJWQCYE = Column(String(40), doc={'zh': '现金及现金等价物期初余额'})
    XJJXJDJWQMYE = Column(String(40), doc={'zh': '现金及现金等价物期末余额'})
    KJZZ = Column(String(40), doc={'zh': '会计准则'})
