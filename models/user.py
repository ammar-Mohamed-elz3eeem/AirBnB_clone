#!/usr/bin/python3
from models.base_model import BaseModel
"""
This module contains declaration of User class that will be
responsible for creating user classes of AirBnB project
"""


class User(BaseModel):
    """
    User: class
    responsible for creating user classes of AirBnB project
    """
    email = ""
    password = ""
    first_name = ""
    user_email = ""
