from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Customer import Customer
from Review import  Review
from Restaurant import Restaurant

##Create an engine and bind it to the Base

engine = create_engine('')
Base.metadata.create_all(engine)

#Create a session

Session = sessionmaker(bind=engine)
Session = Session()



