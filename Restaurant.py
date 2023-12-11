from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name= Column(String)
    reviews = relationship('Review', back_populates='restaurant')

    def restaurant(self):
        return [review.restaurant for review in self.reviews]
    