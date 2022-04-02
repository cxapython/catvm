# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR, DateTime
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class SzseBondMeasureItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'szse_bond_measure'
    desc = '深交所-债券监管措施'

    measure_object = Column(VARCHAR(500), doc={"zh": "监管对象"})
    measure_type = Column(VARCHAR(500), doc={"zh": "类型"})
    letter_no = Column(VARCHAR(500), doc={'zh': '函号'})
    title = Column(VARCHAR(200), doc={"zh": "函件标题"})
    pdf_url = Column(VARCHAR(2000), doc={"zh": "原 pdf_url"})
    pdf_path = Column(VARCHAR(500), doc={"zh": "文件存储地址"})
    letter_date = Column(DateTime, doc={"zh": "发函日期"})
    involved_bonds = Column(VARCHAR(500), doc={"zh": "涉及债券"})
