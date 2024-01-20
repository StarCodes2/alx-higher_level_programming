#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco” from the
database hbtn_0e_100_usa
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

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
