#!/usr/bin/python3
"""
This script contains state class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class State(Base):
    """
    Class with id and name attribute of each state
    """
    __tablename__ = 'states'


    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


    cities = relationship("City", cascade="all, delete-orphan", backref=backref("state", cascade="all"), single_parent=True)
