from sqlalchemy import Column,Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Customer import Customer


Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

id = Column(Integer, primary_key=True)
customer_id = Column(Integer, ForeignKey('customers.id'))
restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
rating = Column(Integer)
customer = relationship('Customer', back_populates='reviews')
restaurant = relationship('Restaurant', back_populates='reviews')

def get_reviews(self):
    return self.reviews

def full_review(self):
    return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars."

