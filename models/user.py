#!/usr/bin/python3
"""A User class to be created"""
from models.base_model import BaseModel


class User(BaseModel):
    """Managing user objects class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
