# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

# engine = create_engine('sqlite:////blogify.db')

# db_session = scoped_session(sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# ))

# Base = declarative_base()

# Base.query = db_session.query_property()


# def init_db():
#     from apps.admin.models *
#     from apps.likes.models *
#     from apps.posts.models *
#     from apps.users.models *

#     Base.metadata.create_all(blind=engine)





