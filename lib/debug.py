from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Restaurant, Customer, Review, restaurant_user

import ipdb

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()
