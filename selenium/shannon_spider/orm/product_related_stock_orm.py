# encoding: utf-8
"""
@author: li qiuhui
@contact: qiuhui_li@shannonai.com

@version: 1.0
@file: product_related_stock.py
@time: 2020/09/27
产业链-产品关联爬虫
"""
from sqlalchemy import Column, VARCHAR, DECIMAL
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ProductRelatedStockItem(CommonFieldMixin, ItemBaseModel):
    '''产业链-产品关联爬虫'''
    __tablename__ = 'product_related_stock'
    desc = '产业链爬虫'

    product = Column(VARCHAR(100), doc={'zh': '产品名称'})
    stock_code = Column(VARCHAR(15), doc={'zh': '证券代码'})
    stock_name = Column(VARCHAR(50), doc={'zh': '证券名称'})
    end_date = Column(VARCHAR(10), doc={'zh': '时间'})
    income_ratio = Column(DECIMAL(6, 3), doc={'zh': '营业收入比重'})
    market_share = Column(DECIMAL(6, 3), index=True, doc={'zh': '市场占有率'})
    product_code = Column(VARCHAR(100), index=True, doc={'zh': '产品代码'})
