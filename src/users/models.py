from sqlalchemy import Integer, String, Column, Boolean
from database import BaseDBModel

class usersT(BaseDBModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, index=True)
    password = Column(String, unique=False, index=False)
    accessToken = Column(String, unique=False, index=False)

class tasksT(BaseDBModel):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_token = Column(String, unique=False, index=True)
    colar_id = Column(Integer, unique=False, index=True)
    text = Column(String, unique=False, index=False)
    taken = Column(Boolean, default=False)

class responsesT(BaseDBModel):
    __tablename__ = "responses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    do_user_id = Column(Integer, unique=False, index=True)
    task_id = Column(Integer, unique=False, index=True)
    answer = Column(String, unique=False)
    readiness = Column(Boolean, default=False)

class subsT(BaseDBModel):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_login = Column(String, unique=False, index=False)
    collar_id = Column(String, unique=False, index=False)
    accessToken = Column(String, unique=False, index=False)
