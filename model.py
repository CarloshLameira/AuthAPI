from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
import datetime


USER = 'root'
PASSWORD = '123321'
HOST = 'localhost'
BANCO = 'Authapi'
PORT = '3306'
CONN = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{BANCO}"
'''engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()'''


Base =  declarative_base()

class User(Base):
        __tablename__ = 'User'
        id = Column(Integer, primary_key=True)
        name = Column(String(50))
        user = Column(String(20))
        password = Column(String(15))

class Tokens(Base):
        __tablename__ = 'Tokens'
        id = Column(Integer, primary_key=True)
        id_user = Column(Integer, ForeignKey('User.id'))
        token = Column(String(100))
        date = Column(DateTime, default=datetime.datetime.utcnow())

#Base.metadata.create_all(engine)