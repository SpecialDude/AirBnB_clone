#!/usr/bin/env python3

"""Definition for the Review model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """AirBnB Review Model"""

    place_id = ""
    user_id = ""
    text = ""
