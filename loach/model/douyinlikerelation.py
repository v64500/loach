# -*- coding: utf-8 -*-
import datetime
from loach.model.base.basemodel import BaseModel
from loach.model import douyindb
from sqlalchemy import Column, Integer, String, DateTime


class DouYinLikeRelation(BaseModel):
    __tablename__ = 'tar_douyin_like_relation'
    __db__ = douyindb
    __key__ = 'user_id'
    __table_args__ = {
        "schema": "douyindb_test"
    }

    #  元数据
    id = Column(Integer, primary_key=True, autoincrement=True, comment=u'记录 id')
    create_time = Column(DateTime, nullable=False,
                         default=datetime.datetime.now, comment=u'记录创建时间')
    # 基本数据，可通过 PC 端获取
    user_id = Column(String, nullable=False, default='', comment=u'作者 id')
    video_id = Column(String, nullable=False, default='', comment=u'')

    @classmethod
    def add(cls, user_id=None, **kwargs):
        obj = cls(user_id=user_id, **kwargs)
        with cls.__db__.session_context(autocommit=True) as session:
            session.add(obj)

    @classmethod
    def exists(cls, user_id=None, video_id=None):
        with cls.__db__.session_context() as session:
            record = session.query(cls).filter(cls.user_id == user_id, cls.video_id == video_id).first()
            if record:
                return True
            else:
                return False
