#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco' from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost;3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_State = State(name='California')
    new_City = City(name='San Franciso')
    new_State.cities.append(new_City)

    session.add(newState)
    session.add(new_City)
    session.commity()
