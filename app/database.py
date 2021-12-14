from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATBASE_URL = 'postgresql://postgres:admin@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATBASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()