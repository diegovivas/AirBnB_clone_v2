#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")

    if os.environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            final = []
            city_list = models.storage.all(City)
            for element in city_list.values():
                if element.state_id == self.id:
                    final.append(element)
            return final
