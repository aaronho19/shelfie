from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

db_string = "postgresql://postgres:postgres@localhost:5432"

db = create_engine(db_string)
base = declarative_base()

class Book(base):
    __tablename__ = 'books'
    #book attributes
    title = Column(String, primary_key=True)
    author = Column(String)
    form = Column(String)
    length = Column(Integer)
    status = Column(String)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    
    
Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

