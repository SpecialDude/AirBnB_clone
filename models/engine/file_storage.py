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

        self.__class__.__objects[obj.id] = obj

    def save(self):
        """serializes all model instances to the JSON file"""

        with open(self.__class__.__file_path, "w") as fd:
            json.dump(self.__class__.__objects, fd)

    def reload(self):
        """loads all models from disk"""

        if os.path.exists(self.__class__.__file_path):
            with open(self.__class__.__file_path) as fd:
                objects = json.load(fd)

            self.__class__.__objects = objects
