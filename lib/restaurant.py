# lib/restaurant.py

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')

    def __repr__(self):
        return f'Restaurant: {self.name}'

    @classmethod
    def fanciest(cls, session):
        return max(session.query(cls).all(), key=lambda restaurant: restaurant.price)

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

    def customers(self):
        return [review.customer for review in self.reviews]
