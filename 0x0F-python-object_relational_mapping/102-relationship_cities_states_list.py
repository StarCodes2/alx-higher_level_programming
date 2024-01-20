#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa
Usage: ./100-relationship_states_cities.py <mysql username>
                                           <mysql password>
                                           <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
