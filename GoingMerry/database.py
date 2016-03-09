from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session

from settings import DB_DIR


Base = declarative_base()
engine = create_engine(DB_DIR, echo=True)
db = scoped_session(sessionmaker(bind=engine))