#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review
import ipdb

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()
