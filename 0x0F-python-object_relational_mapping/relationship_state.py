#!/usr/bin/python3
"""Defines a State model that inherits from SQLAlchemy base and links to the
   MgSQL table state."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Represents the state table for a MySQL Database

    __tablename__ (str): Name of the table in the MySQL database to store state
    id (sqlalchemy.Integer): State's id.
    name (sqlachemy.String): State's name.
    cities (relationship): State - City relationship
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, \
                          delete, delete-orphan")
