#!/usr/bin/python3
import unittest
from models.place import Place
from uuid import uuid4
import datetime
"""unittest for place class
"""


class Testplace(unittest.TestCase):
    """ class for testing place Class """

    def setUp(self):
        self.place = Place()
        self.place.name = "New orliens"
        self.place.description = "This place is awesome"
        self.place.number_bathrooms = 5
        self.place.number_rooms = 3

    def test_place_valid_id(self):
        self.assertIsNotNone(self.place.id)
        self.assertEqual(len(self.place.id), 36)
        self.assertIsInstance(self.place.id, str)

    def test_place_valid_created_date(self):
        self.assertIsNotNone(self.place.created_at)

    def test_place_typeof_created_at(self):
        self.assertIsInstance(self.place.created_at, datetime.datetime)

    def test_place_valid_updated_date(self):
        self.assertIsNotNone(self.place.updated_at)

    def test_place_typeof_updated_at(self):
        self.assertIsInstance(self.place.updated_at, datetime.datetime)

    def test_place_save_method(self):
        time_now = datetime.datetime.now()
        self.assertLessEqual(self.place.updated_at, time_now)
        self.place.save()
        self.assertGreaterEqual(self.place.updated_at, time_now)

    def test_place_to_dict_method(self):
        d = self.place.to_dict()
        self.assertEqual(d['__class__'], "Place")

    def test_creating_placemodel_obj_from_dictionary(self):
        d = self.place.to_dict()
        newobj = Place(**d)
        self.assertEqual(d['name'], newobj.name)


if __name__ == '__main__':
    unittest.main()
