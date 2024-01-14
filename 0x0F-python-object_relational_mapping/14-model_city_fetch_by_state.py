#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa
Usage: ./14-model_city_fetch_by_state.py <mysql username>
                                         <mysql password>
                                         <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).join(City, State.id == City.state_id) \
                        .order_by(City.id):
        print("{}: ({}) {}".format(State.name, City.id, City.name))
