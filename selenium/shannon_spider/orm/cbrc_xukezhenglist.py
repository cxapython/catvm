# encoding: utf-8
from sqlalchemy import Column, String
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class CbrcXukezhenglistItem(CommonFieldMixin, ItemBaseModel):
    """
    银监会许可机构信息爬虫数据表结构
    """
    __tablename__ = "cbrc_xukezhenglist"
    desc = "银监会许可机构信"
    INSTITUTION_CODE = Column(String(20), doc={"zh": "机构编码"})
    SERIAL_NUMBER = Column(String(20), doc={"zh": "证件流水号"})
    INSTITUTION_NAME = Column(String(100), doc={"zh": "机构名称"})
    CATEGORY = Column(String(40), doc={"zh": "机构类型"})
    APPROVAL_DATE = Column(String(20), doc={"zh": "批准成立日期"})
    ISSUE_DATE = Column(String(20), doc={"zh": "发证日期"})
