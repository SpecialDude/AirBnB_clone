#!/usr/bin/env python3

"""This defines the base class for all models"""


import uuid
import datetime
from models import storage


class BaseModel:
    """Base class for AirBnB models"""

    def __init__(self, *args, **kwargs):
        """Instance initialization"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of class"""

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates model on disk"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the json representation of class"""

        data = self.__dict__.copy()

        data["__class__"] = self.__class__.__name__
        data["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        data["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return data
