#!/usr/bin/python3
"""Defines a City model that inherits from SQLAlchemy base and links to the
   MgSQL table city."""
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents the cities table for a MySQL Database

    __tablename__ (str): Name of the table in the MySQL database to store state
    id (sqlalchemy.Integer): City's id.
    name (sqlachemy.String): City's name.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(states.id), nullable=False)
