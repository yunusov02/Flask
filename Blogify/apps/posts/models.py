from typing import List, Optional
from datetime import datetime, timezone

from sqlalchemy import (
    ForeignKey, 
    String, 
    UniqueConstraint, 
    Text, 
    Boolean,
    DateTime,
    func
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)

from database import BaseModel
from ..users.models import User


class Category(BaseModel):

    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)



class Post(BaseModel):

    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
    body: Mapped[str] = mapped_column(Text)
    is_published: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))

    user: Mapped["User"] = relationship("User", foreign_keys=[user_id], backref="posts")
    category: Mapped["Category"] = relationship("Category", foreign_keys=[category_id], backref="posts")



class SchedulePost(BaseModel):

    __tablename__ = 'schedule_post'

    id: Mapped[int] = mapped_column(primary_key=True)
    publish_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))

    post: Mapped["Post"] = relationship("Post", foreign_keys=[post_id], backref="schedule_posts")


class MediaFiles(BaseModel):
    
    __tablename__ = 'mediafiles'

    id: Mapped[int] = mapped_column(primary_key=True)
 
    media_url: Mapped[str] = mapped_column(Text)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))

    post: Mapped["Post"] = relationship("Post", foreign_keys=[post_id], backref="media_posts")


