#!/usr/bin/python3
from models.base_model import BaseModel
"""
This module contains declaration of Review class that will be
responsible for creating Review classes of AirBnB project
"""


class Review(BaseModel):
    """
    Review: class
    responsible for creating Review classes of AirBnB project
    """
    place_id = ""
    user_id = ""
    text = ""
