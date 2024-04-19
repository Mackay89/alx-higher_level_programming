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
            if len(sys.argv) != 5:
                print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
                sys.exit(1)


            try:
                engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
                Base.metadata.create_all(engine)
                Session = sessionmaker(bind=engine)
                session = Session()
                for state in session.query(State).order_by(State.id):
                    print(state.id, state.name, sep=": ")
                    for city in state.cities:
                        print("  {} : {}".format(city.id, city.name))
                session.close()
            except Exception as e:
                print("An error occurred:", e)
