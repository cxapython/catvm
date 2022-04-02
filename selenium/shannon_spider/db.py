# -*- coding: utf-8 -*-
import logging
import sqlparse
import scrapy

from sqlalchemy import create_engine, Table, MetaData, Column, ForeignKey, CHAR
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker, scoped_session, mapper
from sqlalchemy.types import Integer, String, Date, DateTime, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.orm.query import Query
from sqlalchemy.schema import Index

from scrapy.utils.project import get_project_settings


settings = get_project_settings()

#####################################################

ItemBaseModel = declarative_base()  # ItemBaseModel这是所有Item的基类

class CommonFieldMixin(object):
    '''
    所有orm model 必须mixin这些公有的字段
    '''
    id = Column(Integer, primary_key=True, autoincrement=True)
    url_sha = Column(CHAR(40), index=True, nullable=False)
    sha = Column(CHAR(40), index=True, unique=True, nullable=True)

engine = create_engine(
        settings['CRAWLED_DATABASE'],
        pool_recycle=3600,
        pool_pre_ping=True,
        isolation_level='READ_COMMITTED'
        )

session_factory = sessionmaker(
        bind=engine,
        autocommit=False, # Attention: autocommit 应该关闭
        expire_on_commit=False
        )
Session = scoped_session(session_factory)


######################################################

metadata = MetaData(bind=engine)

class DynamicBaseModel(object): pass # 将动态创建的table类绑定到动态生成的类 (基类是DynamicBaseModel) 上

history_item_model = {}

def create_table(ItemModel):
    '''
    创建爬虫所需的表, 分成以下两种:
    1. result table: 用户必须自定义. 保存抓取到的item结果, 一般包含title, content, url, filepath 等
    2. history table: 自动创建,无需定义. 保存抓取历史, 用于去重, 包含请求的sha, json 表示, 最后更新时间, 过期时间等
    ATTENTION: 每个请求只会保留一条记录
    '''
    if not issubclass(ItemModel, CommonFieldMixin):
        raise ValueError('ItemModel: {} must mixin {}'.format(ItemModel.__name__, CommonFieldMixin.__name__))

    if not issubclass(ItemModel, ItemBaseModel):
        raise ValueError("ItemModel: {} must be subclass of {}".format(ItemModel.__name__, ItemBaseModel.__name__))

    if not engine.dialect.has_table(engine, ItemModel.__tablename__):
        # 表不存在, 添加create_at和update_at字段, 并建表
        # 创建 result table
        ItemModel.create_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), doc="创建时间", comment="创建时间")
        ItemModel.update_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), doc="更新时间", comment="更新时间")
        ItemModel.__table__.create(bind=engine, checkfirst=True)

    # 创建 history table
    table = Table(ItemModel.__tablename__ + '_history', metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('url_sha', CHAR(40), index=True, nullable=False, comment='请求的哈希值'),
            Column('req_repr', String(3072), nullable=False, comment='请求的具体内容, 用json表示'),
            Column('last_updated', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment='最后一次更新时间'),
            Column('expire', Integer, nullable=False, server_default=text('-1'), comment='有效期(秒), last_updated + expire 是过期时间, -1 表示永不过期'),
        )
    table.create(bind=engine, checkfirst=True)

    # 保存 history tablename -> HistoryItemModel 的映射
    HistoryItemModel = type(str(table.fullname), (DynamicBaseModel,), {})
    HistoryItemModel.metadata = metadata
    mapper(HistoryItemModel, table)
    history_item_model[ItemModel] = HistoryItemModel


def query_to_sql(query):
    if not isinstance(query, Query):
        raise ValueError('query: %s, must be instance of %s' % (type(query).__name__, scrapy.Request.__name__))
    dialect = query.session.get_bind().dialect
    compiled = query.statement.compile(dialect=dialect, compile_kwargs={'literal_binds': True})
    return sqlparse.format(str(compiled), reindent=True, keyword_case='upper')
