# -*- coding: utf-8 -*-
import datetime
from loach.model.base.basemodel import BaseModel
from loach.model import douyindb
from sqlalchemy import Column, Boolean, Integer, String, DateTime, Date, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB


class DouYinAccount(BaseModel):
    __tablename__ = 'tar_douyin_account_info_mul'
    __db__ = douyindb
    __key__ = 'user_id'
    __table_args__ = {
        "schema": "douyindb_test"
    }

    #  元数据
    id = Column(Integer, primary_key=True, autoincrement=True, comment=u'记录 id')
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now, comment=u'记录创建时间')
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment=u'记录更新时间')

    # 基本数据，可通过 PC 端获取
    user_id = Column(String, nullable=False, default='', comment=u'唯一标识，可用于拼接首页 url')
    description = Column(String, nullable=False, default='', comment=u'原 signature，自我介绍')
    nickname = Column(String, nullable=False, default='', index=True, comment=u'昵称')
    short_id = Column(String, nullable=False, default='', comment=u'疑似抖音分配的自增id')
    douyin_id = Column(String, nullable=False, default='', comment=u'初始为short_id，用户可修改')

    avatar = Column(String, nullable=False, default='', comment=u'头像 url')
    verification = Column(String, nullable=False, default='', comment=u'原 custom_verify，个人认证信息')
    verification_type = Column(Integer, nullable=False, default=0, comment=u'原 custom_verify，个人认证信息')
    birthday = Column(String, nullable=False, default='', comment=u'生日')
    age = Column(Integer, nullable=False, default=0, comment=u'年龄')
    sex = Column(Integer, nullable=False, default=0, comment=u'原 gender，性别')
    region = Column(String, nullable=False, default='', comment=u'原 location，位置')

    liked_count = Column(Integer, nullable=False, default=0, comment=u'总收到赞数')
    video_count = Column(Integer, nullable=False, default=0, comment=u'总作品/视频数')
    like_count = Column(Integer, nullable=False, default=0, comment=u'总赞的作品数')
    music_count = Column(Integer, nullable=False, default=10, comment=u'总音乐数，仅音乐人有该值')
    music_like_count = Column(Integer, nullable=False, default=0, comment=u'总喜欢音乐数，仅音乐人有该值')
    music_used_count = Column(Integer, nullable=False, default=0, comment=u'总使用音乐数，仅音乐人有该值')
    following_num = Column(Integer, nullable=False, default=0, comment=u'关注人数')
    follower_num = Column(Integer, nullable=False, default=0, comment=u'粉丝人数')
    account_create_time = Column(DateTime, nullable=False, default=datetime.datetime(1970, 1, 1), comment=u'账号创建时间')
    like_videos = Column(JSONB, nullable=False, default=list, comment=u'喜欢视频列表')
    videos = Column(JSONB, default=list, comment=u'作品/视频列表')
    musics = Column(JSONB, default=list, comment=u'音乐列表')
    status = Column(Integer, nullable=False, default=0, comment=u'0 表示正常，其他有待定义')
    last_basic_info_time = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # 高级数据，必须通过移动端获取
    following_list = Column(JSONB, default=list, comment=u'关注用户列表')
    follower_list = Column(JSONB, default=list, comment=u'粉丝列表')
    last_advance_info_time = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # 需要计算的数据
    word_cloud = Column(JSONB, nullable=False, default=dict)

    @classmethod
    def add(cls, user_id=None, **kwargs):
        obj = cls(user_id=user_id, **kwargs)
        with cls.__db__.session_context(autocommit=True) as session:
            session.add(obj)

    @classmethod
    def exists(cls, user_id):
        if cls.get(user_id):
            return True
        else:
            return False
    #
    # def delete(cls, user_id):
