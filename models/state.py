#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
storage_engine = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ class to represent states of cities"""
    if (storage_engine == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """cities list
            """
            result = []
            for j, i in models.storage.all(models.city.City).items():
                if (i.state_id == self.id):
                    result.append(i)
            return result
