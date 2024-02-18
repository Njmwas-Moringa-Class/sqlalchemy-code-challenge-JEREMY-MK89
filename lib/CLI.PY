import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Review, Customer, Restaurant

# Replace 'your_module_name' with the actual name of the module where your SQLAlchemy models are defined

engine = create_engine('sqlite:///db/restaurants.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--first_name', prompt='First Name', help='Customer\'s first name')
@click.option('--last_name', prompt='Last Name', help='Customer\'s last name')
def add_customer(first_name, last_name):
    session = Session()
    new_customer = Customer(first_name=first_name, last_name=last_name)
    session.add(new_customer)
    session.commit()
    print(f'Customer {first_name} {last_name} added successfully.')

@cli.command()
@click.option('--name', prompt='Restaurant Name', help='Name of the restaurant')
@click.option('--price', prompt='Price Range', type=int, help='Price range of the restaurant')
def add_restaurant(name, price):
    session = Session()
    new_restaurant = Restaurant(name=name, price=price)
    session.add(new_restaurant)
    session.commit()
    print(f'Restaurant {name} added successfully.')

# You can add more commands for managing reviews, querying data, etc.

if __name__ == '__main__':
    cli()
