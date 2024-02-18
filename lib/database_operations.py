from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Restaurant, Review

engine = create_engine('sqlite:///db/restaurants.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_customer(first_name, last_name):
    customer = Customer(first_name=first_name, last_name=last_name)
    session.add(customer)
    session.commit()

def add_restaurant(name, price):
    restaurant = Restaurant(name=name, price=price)
    session.add(restaurant)
    session.commit()

def add_review(comment, star_rating, restaurant_id, customer_id):
    review = Review(comment=comment, star_rating=star_rating, restaurant_id=restaurant_id, customer_id=customer_id)
    session.add(review)
    session.commit()

def update_customer(customer_id, new_first_name, new_last_name):
    customer = session.query(Customer).get(customer_id)
    if customer:
        customer.first_name = new_first_name
        customer.last_name = new_last_name
        session.commit()

def update_restaurant(restaurant_id, new_name, new_price):
    restaurant = session.query(Restaurant).get(restaurant_id)
    if restaurant:
        restaurant.name = new_name
        restaurant.price = new_price
        session.commit()

def update_review(review_id, new_comment, new_star_rating):
    review = session.query(Review).get(review_id)
    if review:
        review.comment = new_comment
        review.star_rating = new_star_rating
        session.commit()

def delete_customer(customer_id):
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()

def delete_restaurant(restaurant_id):
    restaurant = session.query(Restaurant).get(restaurant_id)
    if restaurant:
        session.delete(restaurant)
        session.commit()

def delete_review(review_id):
    review = session.query(Review).get(review_id)
    if review:
        session.delete(review)
        session.commit()
