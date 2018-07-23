# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base


Modle = declarative_base()


class BaseModel(Modle):
    __abstract__ = True
    __key__ = None
    __db__ = None

    @classmethod
    def get(cls, key):
        with cls.__db__.session_context() as session:
            record = session.query(cls).filter(getattr(cls, cls.__key__) == key).first()
            if record:
                return record

    @classmethod
    def gets(cls, key):
        with cls.__db__.session_context() as session:
            records = session.query(cls).filter_by(getattr(cls, cls.__key__) == key).all()
            if records:
                return records
