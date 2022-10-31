#!/usr/bin/env python

"""Definition of a FileStore class for saving model instancess"""


import json
import os


class FileStorage:
    """A class to handle saving of instance models to disk"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all created model instances"""

        return self.__class__.__objects

    def new(self, obj):
        """adds a new model instance

        Args:
            obj: Model instance to be added
        """

        o_id = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.__class__.__objects[o_id] = obj

    def save(self):
        """serializes all model instances to the JSON file"""
        objects = {
            key: value.to_dict() for key, value in
            self.__class__.__objects.items()
        }

        with open(self.__class__.__file_path, "w") as fd:
            json.dump(objects, fd, indent=4)

    def reload(self):
        """loads all models from disk"""

        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review

        if os.path.exists(self.__class__.__file_path):
            try:
                with open(self.__class__.__file_path) as fd:
                    objects = json.load(fd)
            except Exception as e:
                return

            for key, value in objects.items():
                class_name = value['__class__']
                obj = eval(class_name)(**value)
                self.new(obj)
