# -*- encoding: utf-8 -*-

from sqlalchemy import Column, VARCHAR, DECIMAL, Integer, String
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class LianjiaCommunityItem(CommonFieldMixin, ItemBaseModel):
    """
    链家网爬取小区信息
    """
    __tablename__ = 'lianjia_community'

    COMMUNITY_ID = Column(String(20), doc={'zh': '小区ID'})
    TITLE = Column(String(40), doc={'zh': '小区名字'})
    TAGLIST = Column(String(100), doc={'zh': '小区标签'})
    BIZCIRCLE = Column(String(30), doc={'zh': '小区商圈'})
    LINK = Column(String(100), doc={'zh': '小区链接'})
    DISTRICT = Column(String(100), doc={'zh': '小区位置'})
    PRICE = Column(String(20), doc={'zh': '参考均价'})
    YEAR = Column(String(30), doc={'zh': '建筑年代'})
    HOUSETYPE = Column(String(40), doc={'zh': '建筑类型'})
    ONSALE = Column(String(50), doc={'zh': '出售'})
    ONRENT = Column(String(50), doc={'zh': '在租'})
    BUILDING_NUM = Column(String(30), doc={'zh': '楼栋总数'})
    HOUSE_NUM = Column(String(30), doc={'zh': '房屋总数'})
    COST = Column(String(50), doc={'zh': '物业费用'})
    SERVICE = Column(String(70), doc={'zh': '物业公司'})
    COMPANY = Column(String(70), doc={'zh': '开发商'})
