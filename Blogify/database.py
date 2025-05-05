from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, Integer

from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


engine = create_engine('sqlite:////blogify.db')

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()

    def restore(self):
        self.deleted_at = None
    
    @classmethod
    def all(cls, session):
        return session.query(cls).filter(cls.deleted_at == None)
    
    @classmethod
    def with_deleted(cls, session):
        return session.query(cls)


def init_db():
    # from apps.admin.models *
    # from apps.likes.models *
    # from apps.posts.models *
    # from apps.users.models *

    Base.metadata.create_all(blind=engine)





