#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    new = State(name='Louisiana')
    session.add(new)
    state = session.query(State).filter_by(name='Louisiana').first()
    print(state.id)
    session.commit()
    session.close()
