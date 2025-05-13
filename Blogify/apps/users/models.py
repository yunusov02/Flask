from typing import List, Optional
from sqlalchemy import ForeignKey, String, UniqueConstraint

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)

from database import BaseModel


class User(BaseModel):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String)

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User <{self.username}>'
    

class Followers(BaseModel):
    
    __tablename__ = "followers"

    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    following_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    follower: Mapped["User"] = relationship("User", foreign_keys=[follower_id], backref="following")
    following: Mapped["User"] = relationship("User", foreign_keys=[following_id], backref="followers")

    __table_args__ = (
        UniqueConstraint('follower_id', 'following_id', name='uix_1'),
    )

