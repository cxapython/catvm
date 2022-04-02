# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, TEXT, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class QianFanAppActivityItem(CommonFieldMixin, ItemBaseModel):
    """qian_fan_app_activity"""

    __tablename__ = 'qianfan_app_activity_crawled'

    desc = 'qianfan_app_activity_crawled'
    # app名称
    APP_NAME = Column(String(40), doc={'zh', 'app名称'})

    # 归属公司
    DEVELOP_COMPANY_ABBR = Column(String(40), doc={'zh', '归属公司'})

    # 所属种类
    CATEGORY_NAME = Column(String(40), doc={'zh', '所属种类'})

    # DATE_TYPE
    DATE_TYPE = Column(String(20), doc={'zh', 'DATE_TYPE'})

    # STAT_DATE
    STAT_DATE = Column(Date, doc={'zh', 'STAT_DATE'})

    # 活跃量
    ACTIVE_NUMS = Column(Numeric(30, 20), doc={'zh', '活跃量'})

    # 启动量
    LAUNCH_NUMS = Column(Numeric(30, 20), doc={'zh', '启动量'})

    # 运行时间
    RUNTIME_NUMS = Column(Numeric(30, 20), doc={'zh', '运行时间'})



