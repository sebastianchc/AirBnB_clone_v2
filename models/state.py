#!/usr/bin/python3
"""This is the state class"""
import models
from os import environ
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """return the list of City instances with state_id=State.id
            """
            list_cities = []
            state_cities = models.storage.all(City)
            for st_city in state_cities.values():
                if st_city.state_id == self.id:
                    list_cities.append(st_city)
            return list_cities
