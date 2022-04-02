# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SeeBondProspectusItem(CommonFieldMixin, ItemBaseModel):
    '''上海证券交易所募集说明书'''
    __tablename__ = 'sse_bond_prospectus'
    desc = '上海证券交易所募集说明书'

    ANNOUNCEMENT_TITLE = Column(VARCHAR(500), doc={'zh': '公告标题'})
    ANNOUNCEMENT_TIME = Column(DATETIME, doc={'zh': '公告时间'})
    FILE_URL = Column(VARCHAR(1000), doc={'zh': '文档链接'})
    SAVE_PATH = Column(VARCHAR(1000), doc={'zh': 'OSS路径 '})
