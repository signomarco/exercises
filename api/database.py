from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
