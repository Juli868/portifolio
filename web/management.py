#!/usr/bin/python3
"""Start the tables creation."""
from sqlalchemy import Column, Integer, String
from base_model import BaseModel


class user(BaseModel):
    """Define the attributes of a user."""

    table_name = 'user'
    f_name = Column(String(60), nullable=False)
    l_name = Column(String(60), nullable=False)
    mail = Column(String(120), nullable=False, unique=True)
    pwd = Column(string(60), nullable=False)

    def __init__(fname, lname, mail, password):
        """Initialise the class attributes."""
        self.f_name = fname
        self.l_name = lname
        self.mail = mail
        self.pwd = password
