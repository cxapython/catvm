# encoding: utf-8
"""
@author: li qiuhui
@contact: qiuhui_li@shannonai.com

@version: 1.0
@file: industry_chain.py
@time: 2020/09/22
产业链爬虫
"""
from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class IndustryChainItem(CommonFieldMixin, ItemBaseModel):
    '''产业链爬虫'''
    __tablename__ = 'industry_chain'
    desc = '产业链爬虫'

    from_node = Column(VARCHAR(100), doc={'zh': '起始节点'})
    to_node = Column(VARCHAR(100), doc={'zh': '到达节点'})
    relation = Column(VARCHAR(20), doc={'zh': '关系'})
    relation_type = Column(VARCHAR(20), doc={'zh': '关系类型'})
    importance = Column(VARCHAR(20), doc={'zh': '关系重要性'})
    from_node_code = Column(VARCHAR(100), index=True, doc={'zh': '起始节点产品代码'})
    to_node_code = Column(VARCHAR(100), index=True, doc={'zh': '到达节点产品代码'})
