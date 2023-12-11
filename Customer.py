from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative  import declarative_base


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name=Column(String)
    reviews = relationship('Review', back_populates='customer')
