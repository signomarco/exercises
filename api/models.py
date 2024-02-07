from sqlalchemy import Column, Integer, String
from database import Base


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, index=True)


# class Item(Base):
#     __tablename__ = "items"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=True)
#     price = Column(Float, index=True)
#     tax = Column(Float, index=True)
    

# class Image(Base):
#     __tablename__ = "images"
#     id = Column(Integer, primary_key=True, index=True)
#     url = Column(String, index=True)
#     description = Column(String, index=True)
    

# class Tag(Base):
#     __tablename__ = "tags"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=True)
    