#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """return the list of City instances with state_id=State.id
        """
        list_cities = []
        state_cities = models.engine.all(City)
        for st_city in state_cities.values():
            if st_city.state_id == self.id:
                list_cities.append(st_city)
        return list_cities
