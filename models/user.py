#!/usr/bin/env python3

"""Definition for the User model"""

from models.base_model import BaseModel


class User(BaseModel):
    """AirBnB User Model"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
