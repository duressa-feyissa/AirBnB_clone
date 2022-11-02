#!/usr/bin/python3
"""
0x00. AirBnB clone - The City Module
HBNBCommand module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        a class City that inherits from BaseModel
    """
    state_id = ""
    name = ""

