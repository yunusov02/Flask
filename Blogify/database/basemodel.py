from datetime import datetime, timezone
from sqlalchemy import create_engine

from sqlalchemy import (
    DateTime, 
    func
)

from sqlalchemy.orm import (
    scoped_session, 
    sessionmaker, 
    declarative_base,
    Mapped,
    mapped_column,
)

engine = create_engine('sqlite:///blogify.db')

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = db_session.query_property()


class BaseModel(Base):

    # SoftDelete Model
    
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    deleted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now(timezone.utc)

    def restore(self):
        self.deleted_at = None
    
    @classmethod
    def all(cls, session):
        return session.query(cls).filter(cls.deleted_at == None)
    
    @classmethod
    def with_deleted(cls, session):
        return session.query(cls)

