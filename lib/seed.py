# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Restaurant, Review

# Create the engine and bind it to the session
engine = create_engine('sqlite:///db/restaurants.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Seed the database with some initial data
def seed_database():
    # Add customers
    customer1 = Customer(first_name='Jeremy', last_name='kingi')
    customer2 = Customer(first_name='Juma', last_name='ramadhan')
    session.add_all([customer1, customer2])

    # Add restaurants
    restaurant1 = Restaurant(name='Restaurant Barak', price=2)
    restaurant2 = Restaurant(name='Restaurant Taribush', price=3)
    session.add_all([restaurant1, restaurant2])

    # Add reviews
    review1 = Review(comment='Great food!', star_rating=5, restaurant=restaurant1, customer=customer1)
    review2 = Review(comment='Average experience.', star_rating=3, restaurant=restaurant2, customer=customer2)
    session.add_all([review1, review2])

    # Commit changes to the database
    session.commit()

if __name__ == '__main__':
    # Run the seed function when the script is executed
    seed_database()
