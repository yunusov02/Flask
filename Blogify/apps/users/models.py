from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)


from ...database import BaseModel

class User(BaseModel):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=None)

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User <{self.username}>'
    

class Followers(BaseModel):
    id = Column(Integer, primary_key=True)
