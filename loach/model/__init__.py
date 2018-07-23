# -*- coding: utf-8 -*-
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.local import get_ident
from loach.setting import config


class DatabaseManager(object):
    def __init__(self):
        self.databases = []

    def add_db(self, db):
        self.databases.append(db)

    def teardown_session(self):
        for db in self.databases:
            db.Session.remove()


database_manager = DatabaseManager()


class Database(object):
    def __init__(self, uri, **kwargs):
        self.engine = create_engine(uri, **kwargs)

        self.Session = scoped_session(sessionmaker(
            autocommit=False, autoflush=True, bind=self.engine
        ), scopefunc=get_ident)
        database_manager.add_db(self)

    @property
    def session(self):
        return self.Session()

    @contextmanager
    def session_context(self, autocommit=False):
        session = self.session
        try:
            yield session
            if autocommit:
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


douyindb = Database(
    config['SQLALCHEMY_DATABASE_URI'],
    max_overflow=20,
    pool_size=10,
    pool_timeout=4,
    pool_recycle=3600
)