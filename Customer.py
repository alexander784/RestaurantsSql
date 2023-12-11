from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative  import declarative_base


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    name=Column(String)
    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
         return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
         if not self.reviews:
              return None
         return max(self.reviews, key=lambda review:review.rating).restaurant
    
    def add_review(self, restaurant, rating):
        new_review = Review(customer =self, restaurant=restaurant, rating= rating)
        self.reviews.append(new_review)

    def delete_reviews(self,restaurant):
         self.reviews= [review for review in self.reviews if review.restaurant != restaurant]
         


    
    

    
