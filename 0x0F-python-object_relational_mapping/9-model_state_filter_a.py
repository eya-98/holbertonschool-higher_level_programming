#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
"""
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Ses = sessionmaker(bind=engine)
    session = Ses()
    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(
            State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
