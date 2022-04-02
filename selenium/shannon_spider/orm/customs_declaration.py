# encoding: utf-8
"""
@author: ZhangPei
@file: customs_declaration.py
@time: 2018/8/24 11:31

"""
from sqlalchemy import Column, Text, VARCHAR

from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CustomsDeclarationItem(CommonFieldMixin, ItemBaseModel):
    ''' 俄文海关商品信息'''
    __tablename__ = 'customs_declaration'
    goods_name_ru = Column(Text(), doc={'zh': '商品名称(俄文)'})
    goods_name_zh = Column(Text(), doc={'zh': '商品名称(中文)'})
    hs_code = Column(VARCHAR(200), doc={'zh': 'HS编码'})
    level = Column(VARCHAR(200), doc={'zh': '级别'})
    category_1_ru = Column(Text(), doc={'zh': '所属类别1(俄文)'})
    category_1_zh = Column(Text(), doc={'zh': '所属类别1(中文)'})
    category_2_ru = Column(Text(), doc={'zh': '所属类别2(俄文)'})
    category_2_zh = Column(Text(), doc={'zh': '所属类别2(中文)'})
    category_3_ru = Column(Text(), doc={'zh': '所属类别3(俄文)'})
    category_3_zh = Column(Text(), doc={'zh': '所属类别3(中文)'})
    category_4_ru = Column(Text(), doc={'zh': '所属类别4(俄文)'})
    category_4_zh = Column(Text(), doc={'zh': '所属类别4(中文)'})
    category_5_ru = Column(Text(), doc={'zh': '所属类别5(俄文)'})
    category_5_zh = Column(Text(), doc={'zh': '所属类别5(中文)'})
    category_6_ru = Column(Text(), doc={'zh': '所属类别6(俄文)'})
    category_6_zh = Column(Text(), doc={'zh': '所属类别6(中文)'})
    category_7_ru = Column(Text(), doc={'zh': '所属类别7(俄文)'})
    category_7_zh = Column(Text(), doc={'zh': '所属类别7(中文)'})
    tax_rate_ru = Column(Text(), doc={'zh': '税率(俄文)'})
    tax_rate_zh = Column(Text(), doc={'zh': '税率(中文)'})
    url = Column(VARCHAR(300), doc={'zh': '链接'})
