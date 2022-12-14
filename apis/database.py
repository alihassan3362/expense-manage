from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQLALCHAMY_DATABASE_URL='sqlite:///./category.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread": False})


Sessionlocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()
