# encoding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ChinamoneyAnnItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'chinamoney_ann'
    desc = '中国货币网公告下载'
    bond_name = Column(String(100), doc={'zh': '债券全称'})
    bond_abb = Column(String(50), doc={'zh': '债券简称'})
    bond_code = Column(String(10), doc={'zh': '债券code'})
    bond_type = Column(String(50), doc={'zh': '债券类型'})
    ann_name = Column(String(100), doc={'zh': '公告名称'})
    ann_type = Column(String(20), doc={'zh': '公告类型'})
    ann_date = Column(Date, doc={'zh': '公告日期'})
    file_type = Column(String(10), doc={'zh': '文件类型'})
    file_url = Column(String(200), doc={'zh': '文件url'})
    save_url = Column(String(200), doc={'zh': '保存路径'})
