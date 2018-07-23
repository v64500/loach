# -*- coding: utf-8 -*-
import datetime
from loach.model.base.basemodel import BaseModel
from loach.model import douyindb
from sqlalchemy import Column, Boolean, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSONB


class DouComment(BaseModel):
    __tablename__ = 'tar_douyin_comment_info'
    __db__ = douyindb
    __key__ = 'comment_id'
    __table_args__ = {
        "schema": "douyindb_test"
    }

    #  元数据
    id = Column(Integer, primary_key=True, autoincrement=True, comment=u'记录 id')
    create_time = Column(DateTime, nullable=False,
                         default=datetime.datetime.now, comment=u'记录创建时间')

    # 基本数据，可通过 PC 端获取
    # TODO：user_id 和 short_id 二者必须有一个，且需要根据账号表定期清洗补全
    user_id = Column(String, nullable=False, default='', comment=u'作者 id')
    short_id = Column(String, nullable=False, default='', comment=u'作者短 id')
    nickname = Column(String, nullable=False, default='', comment=u'作者昵称')
    video_id = Column(String, nullable=False, default='', comment=u'视频唯一标识')
    reply_id = Column(String, nullable=False, default='', comment=u'回复的评论的id')
    comment_id = Column(String, nullable=False, unique=True, comment=u'视频唯一标识')
    text = Column(String, nullable=False, default='', comment=u'评论内容')
    like_count = Column(Integer, nullable=False, default=0, comment=u'原 digg_count，点赞数')
    status = Column(Integer, nullable=False, default=0, comment=u'0 表示正常，其他有待定义')
    comment_create_time = Column(DateTime, default=datetime.datetime(1970, 1, 1), comment=u'视频创建时间')

    @classmethod
    def add(cls, **kwargs):
        obj = cls(**kwargs)
        with cls.__db__.session_context(autocommit=True) as session:
            session.add(obj)

    @classmethod
    def exists(cls, comment_id):
        if cls.get(comment_id):
            return True
        else:
            return False

    @classmethod
    def update(cls, **kwargs):
        assert cls.__key__ in kwargs.keys(), '待更新记录里应包含 %s' % cls.__key__
        with cls.__db__.session_context(autocommit=True) as session:
            records = session.query(cls).filter(cls.user_id == kwargs['video_id'])
            if records:
                rows_count = records.update({k: v for k, v in kwargs.items()})
                return rows_count

    @classmethod
    def upsert(cls, **kwargs):
        assert cls.__key__ in kwargs.keys(), '待更新记录里应包含 %s' % cls.__key__
        record = cls.get(kwargs[cls.__key__])
        if not record:
            cls.add(**kwargs)
        else:
            cls.update(**kwargs)
