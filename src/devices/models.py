from sqlalchemy import Integer, String, Column
from database import BaseDBModel

class dogsT(BaseDBModel):
    __tablename__ = "dogs_with_collars"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=False, index=True)
    collar_id = Column(String, unique=True, index=False)
    collar_token = Column(String, unique=True, index=False)


