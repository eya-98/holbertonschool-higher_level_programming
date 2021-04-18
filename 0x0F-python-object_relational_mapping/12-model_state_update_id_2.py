#!/usr/bin/python3
"""
changes the name of a State object from the database 
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Ses = sessionmaker(bind=engine)
    session = Ses()
    state = session.query(State).filter(id=2).first()
    state.name ="New Mexico"
    session.commit()
    session.close()
