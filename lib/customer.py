
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    reviews = relationship('Review', back_populates='customer')

    def __repr__(self):
        return f'Customer: {self.first_name} {self.last_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def favorite_restaurant(self):
        return max(self.reviews, key=lambda review: review.star_rating).restaurant

    def add_review(self, restaurant, rating, session):
        new_review = Review(star_rating=rating, customer=self, restaurant=restaurant)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant, session):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

    def reviews(self):
        return self.reviews

    def restaurants(self):
        return [review.restaurant for review in self.reviews]
