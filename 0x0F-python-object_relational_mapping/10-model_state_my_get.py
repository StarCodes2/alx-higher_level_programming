#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database
hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all.py <mysql username>
                                    <mysql password>
                                    <database name>
                                    <state name to search>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    for state in session.query(State):
        if argv[4] == state.name:
            print("{}".format(state.id))
            found = True
            break

    if not found:
        print("Not found")
