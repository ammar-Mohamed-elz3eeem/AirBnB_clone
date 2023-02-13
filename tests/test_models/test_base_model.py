#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from uuid import uuid4
import datetime
"""unittest for base model class
"""


class TestBaseModel(unittest.TestCase):
    """ class for testing BaseModel Class """

    def setUp(self):
        self.base = BaseModel()

    def test_valid_id(self):
        self.assertIsNotNone(self.base.id)
        self.assertEqual(len(self.base.id), 36)
        self.assertIsInstance(self.base.id, str)

    def test_valid_created_date(self):
        self.assertIsNotNone(self.base.created_at)

    def test_typeof_created_at(self):
        self.assertIsInstance(self.base.created_at, datetime.datetime)

    def test_valid_updated_date(self):
        self.assertIsNotNone(self.base.updated_at)

    def test_typeof_updated_at(self):
        self.assertIsInstance(self.base.updated_at, datetime.datetime)

    def test_save_method(self):
        time_now = datetime.datetime.now()
        self.assertLessEqual(self.base.updated_at, time_now)
        self.base.save()
        self.assertGreaterEqual(self.base.updated_at, time_now)

    def test_to_dict_method(self):
        d = self.base.to_dict()
        self.assertEqual(d['__class__'], "BaseModel")

    def test_creating_basemodel_obj_from_dictionary(self):
        d = self.base.to_dict()
        newobj = BaseModel(**d)
        self.assertEqual(d['id'], newobj.id)
        self.assertEqual(self.base.created_at, newobj.created_at)


if __name__ == '__main__':
    unittest.main()
