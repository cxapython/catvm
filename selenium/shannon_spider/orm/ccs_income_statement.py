# encoding: utf-8
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: ccs_income_statement.py
@time: 2018/10/20 11:15

中概股
"""
from sqlalchemy import Column, String, Numeric, Date, Time, Integer
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CcsIncomeStatementItem(CommonFieldMixin, ItemBaseModel):
    '''东方财富对中概股综合损益表抓取结果'''
    __tablename__ = 'ccs_income_statement'
    desc = '中概股综合损益表数据'
    CODE = Column(String(40), doc={'zh': '股票代码'})
    NAME = Column(String(40), doc={'zh': '股票名称'})
    BBJZR = Column(String(40), doc={'zh': '日期'})
    CBLX = Column(String(40), doc={'zh': '财表类型'})
    NJR = Column(String(40), doc={'zh': '年结日'})
    BZ = Column(String(40), doc={'zh': '币种'})
    SR = Column(String(40), doc={'zh': '收入'})
    ZYSR = Column(String(40), doc={'zh': '主营收入'})
    QTYWSR = Column(String(40), doc={'zh': '其他业务收入'})
    YYSR = Column(String(40), doc={'zh': '营业收入'})
    CB = Column(String(40), doc={'zh': '成本'})
    ZYCB = Column(String(40), doc={'zh': '主营成本'})
    QTYWCB = Column(String(40), doc={'zh': '其他业务成本'})
    YYCB = Column(String(40), doc={'zh': '营业成本'})
    MLQTXM = Column(String(40), doc={'zh': '毛利其他项目'})
    ML = Column(String(40), doc={'zh': '毛利'})
    JYFY = Column(String(40), doc={'zh': '经营费用'})
    YFFY = Column(String(40), doc={'zh': '研发费用'})
    YXFY = Column(String(40), doc={'zh': '营销费用'})
    YBJXZFY = Column(String(40), doc={'zh': '一般及行政费用'})
    ZJYTX = Column(String(40), doc={'zh': '折旧与摊销'})
    JZJBB = Column(String(40), doc={'zh': '减值及拨备'})
    QTYYFY = Column(String(40), doc={'zh': '其他营业费用'})
    CZFY = Column(String(40), doc={'zh': '重组费用'})
    YYFY = Column(String(40), doc={'zh': '营业费用'})
    QTSY = Column(String(40), doc={'zh': '其他收益'})
    YYLR = Column(String(40), doc={'zh': '营业利润'})
    SQYL = Column(String(40), doc={'zh': '税前溢利'})
    LXSR = Column(String(40), doc={'zh': '利息收入'})
    LXZC = Column(String(40), doc={'zh': '利息支出'})
    QYXTZSY = Column(String(40), doc={'zh': '权益性投资损益'})
    TZXJZZB = Column(String(40), doc={'zh': '投资性减值准备'})
    QTSRZC = Column(String(40), doc={'zh': '其他收入(支出)'})
    GYJJBDSY = Column(String(40), doc={'zh': '公允价值变动损益'})
    HDSY = Column(String(40), doc={'zh': '汇兑损益'})
    ZCCLSY = Column(String(40), doc={'zh': '资产处理损益'})
    RZSRZC = Column(String(40), doc={'zh': '融资收入(支出)'})
    SQLRQTXM = Column(String(40), doc={'zh': '税前利润其他项目'})
    CXJYSQLR = Column(String(40), doc={'zh': '持续经营税前利润'})
    SDS = Column(String(40), doc={'zh': '所得税'})
    CXJYJLR = Column(String(40), doc={'zh': '持续经营净利润'})
    YZZHFCXJYJLR = Column(String(40), doc={'zh': '已终止或非持续经营净利润'})
    SHLRQTXM = Column(String(40), doc={'zh': '税后利润其他项目'})
    JLR = Column(String(40), doc={'zh': '净利润'})
    GDYZYL = Column(String(40), doc={'zh': '股东应占溢利'})
    SSGDSY = Column(String(40), doc={'zh': '少数股东损益'})
    GSYYXGJLRJQTX = Column(String(40), doc={'zh': '归属于优先股净利润及其他项'})
    GSYPTGGDJLR = Column(String(40), doc={'zh': '归属于普通股股东净利润'})
    GDYZYLQTXM = Column(String(40), doc={'zh': '股东应占溢利其他项目'})
    GSYMGSGDJLR = Column(String(40), doc={'zh': '归属于母公司股东净利润'})
    MGZB = Column(String(40), doc={'zh': '每股指标'})
    PTGGX = Column(String(40), doc={'zh': '普通股股息'})
    MGGXPTG = Column(String(40), doc={'zh': '每股股息-普通股'})
    JBMGSYPTG = Column(String(40), doc={'zh': '基本每股收益-普通股'})
    TBMGSYPTG = Column(String(40), doc={'zh': '摊薄每股收益-普通股'})
    JBMGSYADS = Column(String(40), doc={'zh': '基本每股收益-ADS'})
    TBMGSYADS = Column(String(40), doc={'zh': '摊薄每股收益-ADS'})
    QMSY = Column(String(40), doc={'zh': '全面收益'})
    BGSYYRZQMSYZE = Column(String(40), doc={'zh': '本公司拥有人占全面收益总额'})
    FKGQYZQMSYZE = Column(String(40), doc={'zh': '非控股权益占全面收益总额'})
    QTQMSYQTXM = Column(String(40), doc={'zh': '其他全面收益其他项目'})
    QTQMSYHJX = Column(String(40), doc={'zh': '其他全面收益合计项'})
    QMSYQTXM = Column(String(40), doc={'zh': '全面收益其他项目'})
    QMSYZE = Column(String(40), doc={'zh': '全面收益总额'})
    KJZZ = Column(String(40), doc={'zh': '会计准则'})
