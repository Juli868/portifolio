#!/usr/bin/python3
"""Start the tables creation."""
from sqlalchemy import Column, Integer, String
from base_model import BaseModel


class User(BaseModel):
    """Define the attributes of a user."""

    table_name = 'user'
    f_name = Column(String(60), nullable=False)
    l_name = Column(String(60), nullable=False)
    mail = Column(String(120), nullable=False, unique=True)
    pwd = Column(string(60), nullable=False)

    def __init__(self, fname, lname, mail, password):
        """Initialise the class attributes."""
        self.f_name = fname
        self.l_name = lname
        self.mail = mail
        self.pwd = password


class Admin_user(BaseModel):
    table_name = "admin"
    mail


class Airport(BaseModel):
    """Define the atrributes of an airport."""

    country = Column(String(60), nullable=False)
    name = Column(String(60), nullable=False)
    long = Column(Float, nullable=False)
    lat = Column(Float, nullable=False)

    def __init(self, country, name, latitude, longitude):
        self.country = country
        self.name = name
        self.long = longitude
        self.lat = lat


class Flight(BaseModel):
    """Define the attributes of a flight."""

    table_name = 'flight'
    location_fr =\
        Column(String(60), ForeignKey('airport.name'), nullable=False)
    location_to = Column(String(60), ForeignKey('airport.id'), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    trip_class = Column(String(20), nullable=False)

    def __init(self, l_from, l_to, departure, trip_class, amount):
        """Initialise the instance."""
        self.location_fr = l_from
        self.location_to = l_to
        self.departure_time = departure
        self.amount = amount,
        self.trip_class = trip_class
