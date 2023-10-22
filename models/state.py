#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = ""

    @property
    def cities(self):
        """
        Getter method to return the list of City objects linked to the current State.
        """
        from models import storage
        all_cities = storage.all(City)
        return [city for city in all_cities.values() if city.state_id == self.id]
