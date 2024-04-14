#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    else:
        print("Not found")
