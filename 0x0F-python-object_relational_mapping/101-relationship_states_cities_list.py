#!/usr/bin/python3
"""
This script lists all state objects and corresponding City objects in the database hbtn_0e_101_usa.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)


    Session = sessionmaker(bind=engine)
    session = Session()


    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
            
