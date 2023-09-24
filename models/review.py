#!/usr/bin/python3
"""Review class to be created"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Managing review objects class"""

    place_id = ""
    user_id = ""
    text = ""
