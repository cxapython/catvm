# coding: utf-8

from sqlalchemy import Column, String, Numeric, Date, Time, Integer, TEXT, BOOLEAN
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class QianFanAppRankingItem(CommonFieldMixin, ItemBaseModel):
    """qian_fan_app_ranking"""

    __tablename__ = 'qianfan_app_ranking_crawled'

    desc = '千帆App活跃排名'
    # app名称
    APP_NAME = Column(String(100), doc={'zh', 'app名称'})

    # 开发公司
    DEVELOP_COMPANY_ABBR = Column(String(100), doc={'zh', '开发公司'})

    # 发布公司
    PUBLISH_COMPANY_ABBR = Column(String(100), doc={'zh', '发布公司'})

    # game_app
    GAME_APP = Column(BOOLEAN, doc={'zh', 'game_app'})

    # 所属种类
    CATEGORY_NAME = Column(String(40), doc={'zh', '所属种类'})

    # 排名时间
    RANKING_TIME = Column(String(40), doc={'zh', '排名时间'})

    # 排名榜
    RANKING_VALUE = Column(String(20), doc={'zh', '排名榜'})

    # 排名种类
    RANKING_CATEGORY = Column(String(40), doc={'zh', '排名种类'})

    # 活跃量
    ACTIVE_NUMS = Column(Numeric(30, 18), doc={'zh', '活跃量'})

    # 启动量
    LAUNCH_NUMS = Column(Numeric(30, 18), doc={'zh', '启动量'})

    # 运行时间
    RUNTIME_NUMS = Column(Numeric(30, 18), doc={'zh', '运行时间'})

    ACTIVE_NUMS_RATIO = Column(Numeric(30, 20), doc={'zh', 'ACTIVE_NUMS_RATIO'})

    ACTIVE_AVG_DAY = Column(Numeric(30, 20), doc={'zh', 'ACTIVE_AVG_DAY'})

    ACTIVE_AVG_DAY_RATIO = Column(Numeric(30, 20), doc={'zh', 'ACTIVE_AVG_DAY_RATIO'})

    LAUNCH_NUMS_RATIO = Column(Numeric(30, 20), doc={'zh', 'LAUNCH_NUMS_RATIO'})

    LAUNCH_AVG_DAY = Column(Numeric(30, 18), doc={'zh', 'LAUNCH_AVG_DAY'})

    LAUNCH_AVG_DAY_RATIO = Column(Numeric(30, 20), doc={'zh', 'LAUNCH_AVG_DAY_RATIO'})

    LAUNCH_PER_PERSON = Column(Numeric(30, 20), doc={'zh', 'LAUNCH_PER_PERSON'})

    LAUNCH_PER_PERSON_RATIO = Column(Numeric(30, 20), doc={'zh', 'LAUNCH_PER_PERSON_RATIO'})

    LAUNCH_AVG_PERSON = Column(Numeric(30, 20), doc={'zh', 'LAUNCH_AVG_PERSON'})

    LAUNCH_AVG_PERSON_RATIO = Column(Numeric(30, 20), doc={'zh', 'LAUNCH_AVG_PERSON_RATIO'})

    RUNTIME_NUMS_RATIO = Column(Numeric(30, 20), doc={'zh', 'RUNTIME_NUMS_RATIO'})

    RUNTIME_AVG_DAY = Column(Numeric(30, 18), doc={'zh', 'RUNTIME_AVG_DAY'})

    RUNTIME_AVG_DAY_RATIO = Column(Numeric(30, 20), doc={'zh', 'RUNTIME_AVG_DAY_RATIO'})

    RUNTIME_PER_PERSON = Column(Numeric(30, 20), doc={'zh', 'RUNTIME_PER_PERSON'})

    RUNTIME_PER_PERSON_RATIO = Column(Numeric(30, 20), doc={'zh', 'RUNTIME_PER_PERSON_RATIO'})

    RUNTIME_AVG_PERSON = Column(Numeric(30, 20), doc={'zh', 'RUNTIME_AVG_PERSON'})

    RUNTIME_AVG_PERSON_RATIO = Column(Numeric(30, 20), doc={'zh', 'RUNTIME_AVG_PERSON_RATIO'})

    CATE_PERMEABILITY = Column(Numeric(30, 20), doc={'zh', 'CATE_PERMEABILITY'})

    RANKING_LEVEL = Column(Integer, doc={'zh', 'RANKING_LEVEL'})









