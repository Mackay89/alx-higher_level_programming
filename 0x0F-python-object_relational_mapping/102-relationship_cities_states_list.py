#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)


    Session = sessionmaker(bind=engine)
    session = Session()


    for city, state in session.query(City, State).join(State, State.id == City.state_id).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))
                