#!/usr/bin/python3
"""A User class to be created"""

from models.base_model import BaseModel


class City(BaseModel):
    """Managing city objects class"""

    state_id = ""
    name = ""
