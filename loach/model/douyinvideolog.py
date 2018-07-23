# -*- coding: utf-8 -*-
import datetime
from loach.model.base.basemodel import BaseModel
from loach.model import douyindb
from sqlalchemy import Column, Boolean, Integer, String, TIMESTAMP, JSON


class DouYinVideoMonitor(BaseModel):
    """ 通知规则实现，这里置存储面向 APP 的通知，不支持面向用户的通知
    """
    __tablename__ = 'tar_douyin_video_monitor'
    __db__ = douyindb
    __key__ = 'video_id'
    __table_args__ = {
        "schema": "douyin"
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer,  nullable=False)
    video_id = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP, default=datetime.datetime.now().timestamp(), nullable=False)
    comment_count = Column(Integer, nullable=False)
    share_count = Column(Integer, nullable=False)
    like_count = Column(Integer, nullable=False)
    play_count = Column(Integer, nullable=False)
