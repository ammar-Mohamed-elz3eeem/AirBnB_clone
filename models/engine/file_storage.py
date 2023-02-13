#!/usr/bin/python3

from uuid import uuid4
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import datetime
import json
"""
This module contains declaration of FileStorage class that will be
save all other inctances of classes of AirBnB project
"""


class FileStorage:
    """ FileStorage: the saving and retrieving class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        with open(self.__file_path, "w+") as fp:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, fp)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(self.__file_path, 'r') as fp:
                dicts = json.load(fp)
                for value in dicts.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
