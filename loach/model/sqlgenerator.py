# -*- coding: utf-8 -*-

from loach.model.base.basemodel import Modle
from loach.model import douyindb
from sqlalchemy.schema import CreateSchema
# from loach.model.douyinlikerelation import DouYinLikeRelation
# from loach.model.douyinfollowrelation import DouYinFollowRelation
# from loach.model.douyinaccount import DouYinAccount
# from loach.model.douyinvideo import DouYinVideo
from loach.model.douyincomment import DouComment
# from loach.model.douyinaccount_mul import DouYinAccount
# douyindb.engine.execute(CreateSchema('douyindb_test'))
Modle.metadata.create_all(douyindb.engine)
