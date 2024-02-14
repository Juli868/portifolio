#!/usr/bin/python3
"""Data management."""
from table import User, Airport, Flight
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy

classes = {"User": User, "Airport": Airport, "Flight": Flight}


class Storage:
    """interacts with the Mysql database."""

    __engine = None
    __session = None

    def __init(self):
        FLIGHT_USER = getenv('FLIGHT_USER')
        FLIGHT_PWD = getenv('FLIGHT_PWD')
        FLIGHT_HOST = getenv('FLIGHT_HOST')
        FLIGHT_DB = getenv('FLIGHT_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(FLIGHT_USER,
                                             FLIGHT_PWD,
                                             FLIGHT_HOST,
                                             FLIGHT_DB))

    def all(self, cls=None):
        """Querry on the current session."""
        new_dict = {}
        for clss in clasess:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.sesion.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def save(self):
        """Save all changes made during the session."""
        self.__session.commit()

    def new(self, obj):
        """Add a new record to the current session."""
        self.__session.add(obj)

    def delete(self, obj):
        """Delete from the current db session obj if not none."""
        self.__session.delete(obj)

    def reload(self):
        """Reload data from the database."""
        Base.meatadata.create_all(self.__engine)
        sess_factor = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factor)
        self.__session = Session

    def close(self):
        """End session."""
        self.__session.remove()
