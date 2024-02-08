# lib/review.py

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

    def __repr__(self):
        return f'Review: {self.star_rating} stars'

    def full_review(self):
        return f'Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars.'
