#!/usr/bin/python3
"""
defines city class
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class city(Base):
    """definition of city class"""
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
