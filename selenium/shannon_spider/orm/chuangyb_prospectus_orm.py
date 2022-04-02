# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ChuangybProspectusItem(CommonFieldMixin, ItemBaseModel):
    '''创业板招股书爬取'''
    __tablename__ = 'chuangyb_prospectus'
    desc = '创业板招股书爬取'

    ISSURE = Column(VARCHAR(200), doc={'zh': '发行人'})
    PUBLISH_DATE = Column(DATETIME, doc={'zh': '披露日期'})
    FILE_NAME = Column(VARCHAR(500), doc={'zh': '招股书标题'})
    FILE_URL = Column(VARCHAR(1000), doc={'zh': '文档链接'})
    SAVE_PATH = Column(VARCHAR(1000), doc={'zh': 'OSS路径 '})
