#!/usr/bin/python3
"""
0x00. AirBnB clone - The User Module
HBNBCommand module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        a class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
