#!/usr/bin/python3

from uuid import uuid4
import datetime
import models
"""
This module contains declaration of BaseModel class that will be
the parent of all other classes of AirBnB project
"""


class BaseModel:
    """ BaseModel: the parent of all classes in this project """
    def __init__(self, *args, **kwargs):
        if (len(kwargs.items()) > 0):
            for (k, v) in kwargs.items():
                if k == "__class__":
                    continue
                if (k == "updated_at" or k == "created_at"):
                    setattr(self, k, datetime.datetime.
                            strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat(),
        }
