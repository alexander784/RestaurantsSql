from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Customer import Customer
from Review import  Review
from Restaurant import Restaurant

Base = declarative_base()

##Create an engine and bind it to the Base

engine = create_engine('')
Base.metadata.create_all(engine)

#Create a session

Session = sessionmaker(bind=engine)
Session = Session()




