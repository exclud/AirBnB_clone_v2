#!/usr/bin/python3
"""DBStorage Class"""
class DBStorage:
    def close(self):
        """
        Call remove() method on the private session attribute or close() on the Session.
        """
        self.__session.remove()
