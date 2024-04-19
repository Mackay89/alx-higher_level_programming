#!/usr/bin/python3
"""
This script contains the class definition of a City.
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'


    id =  Column(Integer, nullable=False, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
