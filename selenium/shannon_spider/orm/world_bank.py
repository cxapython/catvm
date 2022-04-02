# -*- encoding: utf-8 -*-
"""
@author: peng lei
@contact: me@penglei.com

@version: 1.0
@file: world_bank.py
@time: 2018/11/17 18:15

世界银行国家信息
"""

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer,String
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class WorldBankItem(CommonFieldMixin, ItemBaseModel):

    __tablename__ = 'country_category_crawled_new'

    desc = '国家分类原表'

    COUNTRY_NAME = Column(String(50), doc={'zh': '国家及地区'})
    CATEGORY_NAME = Column(String(50), doc={'zh': '国家类别'})
    CATEGORY_TYPE = Column(String(50), doc={'zh': '分类标准'})
    EXCEL_URL = Column(String(100), doc={'zh': 'excel链接'})
    # OSS_FILEPATH = Column(String(100), doc={'zh': 'OSS上传路径'})
    # OSS_FILENAME = Column(String(100), doc={'zh': 'OSS文件名字'})