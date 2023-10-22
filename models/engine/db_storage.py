#!/usr/bin/python3
"""DBStorage Class"""
import models
from models.base_model import BaseModel, Base
from models import city, state
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None

    """DBStorage class"""
    def close(self):
        """
        Call remove() method on the private session attribute or close() on the Session.
        """
        self.__session.__class__.close(self.__session)
        self.reload()
