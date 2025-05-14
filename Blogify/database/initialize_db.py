from .basemodel import BaseModel, engine

def init_db():
    from apps.users.models import User, Followers
    from apps.posts.models import Post, SchedulePost, MediaFiles
    from apps.likes.models import Comments, Likes, PostViews

    BaseModel.metadata.create_all(bind=engine)

