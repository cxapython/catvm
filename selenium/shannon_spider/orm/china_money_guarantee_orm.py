# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class ChinaMoneyGuaranteeItem(CommonFieldMixin, ItemBaseModel):
    '''货币网担保'''
    __tablename__ = 'china_money_guarantee'
    desc = '货币网担保'

    ANNOUNCEMENT_TITLE = Column(VARCHAR(500), doc={'zh': '公告标题'})
    ANNOUNCEMENT_TIME = Column(DATETIME, doc={'zh': '公告时间'})
    FILE_URL = Column(VARCHAR(1000), doc={'zh': '文档链接'})
    SAVE_PATH = Column(VARCHAR(1000), doc={'zh': 'OSS路径 '})
