# -*- encoding: utf-8 -*-
from sqlalchemy import Column, VARCHAR
from shannon_spider.db import CommonFieldMixin, ItemBaseModel


class LicenseOfDischargingPollutantsItem(CommonFieldMixin, ItemBaseModel):
    __tablename__ = 'License_of_Discharging_Pollutants'
    desc = '排污许可信息'

    License_number = Column(VARCHAR(30), doc={'zh', '许可证编号'})
    name = Column(VARCHAR(50), doc={'zh', '单位名称'})
    industry = Column(VARCHAR(20), doc={'zh', '行业类别'})
    address = Column(VARCHAR(50), doc={'zh', '地址'})
    region = Column(VARCHAR(50), doc={'zh', '所在地区'})
    licence_issuing_authority = Column(VARCHAR(50), doc={'zh', '发证机关'})
    report_type = Column(VARCHAR(30), doc={'zh', '报告类型'})
    report_period = Column(VARCHAR(30), doc={'zh', '报告周期'})
    pdf_url = Column(VARCHAR(750), index=True, doc={'zh', 'pdf路径'})
    SAVE_PATH = Column(VARCHAR(1000), doc={'zh': 'OSS路径 '})
