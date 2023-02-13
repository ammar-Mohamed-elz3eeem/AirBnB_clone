#!/usr/bin/python3
import unittest
from models.city import City
from uuid import uuid4
import datetime
"""unittest for city class
"""


class TestCity(unittest.TestCase):
    """ class for testing city Class """

    def setUp(self):
        self.city = City()
        self.city.name = "Los Anglos"
        self.city.description = "This city is awesome"
        self.city.number_bathrooms = 5
        self.city.number_rooms = 3

    def test_city_valid_id(self):
        self.assertIsNotNone(self.city.id)
        self.assertEqual(len(self.city.id), 36)
        self.assertIsInstance(self.city.id, str)

    def test_city_valid_created_date(self):
        self.assertIsNotNone(self.city.created_at)

    def test_city_typeof_created_at(self):
        self.assertIsInstance(self.city.created_at, datetime.datetime)

    def test_city_valid_updated_date(self):
        self.assertIsNotNone(self.city.updated_at)

    def test_city_typeof_updated_at(self):
        self.assertIsInstance(self.city.updated_at, datetime.datetime)

    def test_city_save_method(self):
        time_now = datetime.datetime.now()
        self.assertLessEqual(self.city.updated_at, time_now)
        self.city.save()
        self.assertGreaterEqual(self.city.updated_at, time_now)

    def test_city_to_dict_method(self):
        d = self.city.to_dict()
        self.assertEqual(d['__class__'], "City")

    def test_creating_citymodel_obj_from_dictionary(self):
        d = self.city.to_dict()
        newobj = City(**d)
        self.assertEqual(d['name'], newobj.name)


if __name__ == '__main__':
    unittest.main()
