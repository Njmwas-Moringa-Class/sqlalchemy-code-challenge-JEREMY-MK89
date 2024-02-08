

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from restaurant import Restaurant
from customer import Customer
from review import Review

# Define Base here
Base = declarative_base()

engine = create_engine('sqlite:///db/restaurants.db', echo=True)
Session = sessionmaker(bind=engine)

# Move this line after defining Base
Base.metadata.create_all(engine)

session = Session()

