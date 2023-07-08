import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import Config


#engine = db.create_engine("", pool_size=20, echo=True)
#connection = engine.connect()

Base = declarative_base()