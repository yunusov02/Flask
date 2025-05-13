from typing import List, Optional
from sqlalchemy import ForeignKey, String, UniqueConstraint

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database import BaseModel
from ..posts.models import Post
from ..users.models import User


class PostViews(BaseModel):

    __tablename__ = 'postviews'

    id: Mapped[int] = mapped_column(primary_key=True)

    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    post: Mapped["Post"] = relationship("Post", foreign_keys=[post_id], backref='postviews')
    user: Mapped["User"] = relationship("User", foreign_keys=[user_id], backref='user_views')


class Likes(BaseModel):

    __tablename__ = 'likes'

    id: Mapped[int] = mapped_column(primary_key=True)
    likes: Mapped[int] = mapped_column(default=1)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))

    post: Mapped["Post"] = relationship("Post", foreign_keys=[post_id], backref='likes')
    user: Mapped["User"] = relationship("User", foreign_keys=[user_id], backref='user_likes')



class Comments(BaseModel):

    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))

    post: Mapped["Post"] = relationship("Post", foreign_keys=[post_id], backref='comments')
    user: Mapped["User"] = relationship("User", foreign_keys=[user_id], backref='user_comments')


