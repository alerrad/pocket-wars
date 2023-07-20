from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import Config


CONNECTION_URL = (
    f"postgresql://{Config.DB_USERNAME}:{Config.DB_PASSWORD}"
    f"@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
)

engine = create_engine(CONNECTION_URL, pool_size=20, echo=False)
session = sessionmaker(bind=engine, autoflush=False)()

Base = declarative_base()