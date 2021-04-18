#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
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
    first = session.query(State).order_by(State.id).first()
    if first is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
    session.close()
