# -*- coding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DATETIME
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class AShareThemeItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'a_share_theme'

    desc = 'A股股票主题'
    # 一级主题名称
    FIRST_LEVEL_THEME = Column(VARCHAR(200), doc={'zh', '一级主题名称'})

    # 二级主题名称
    SECOND_LEVEL_THEME = Column(VARCHAR(200), doc={'zh', '二级主题名称'})

    # 股票代码
    S_INFO_STOCKCODE = Column(VARCHAR(10), doc={'zh', '股票代码'})

    # 公司简称
    S_INFO_NAME = Column(VARCHAR(200), doc={'zh', '公司简称'})

    # 网页链接
    URL = Column(VARCHAR(200), doc={'zh', '网页链接'})
    CREATE_TIME = Column(DATETIME, doc={'zh': '更新时间'})
