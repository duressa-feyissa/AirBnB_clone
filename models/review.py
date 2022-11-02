#!/usr/bin/python3
"""
0x00. AirBnB clone - The Review Module
HBNBCommand module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        a class Review that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

