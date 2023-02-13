#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from uuid import uuid4
import datetime
"""unittest for Amenity class
"""


class TestAmenity(unittest.TestCase):
    """ class for testing Amenity Class """

    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "Los Anglos"
        self.amenity.description = "This amenity is awesome"
        self.amenity.number_bathrooms = 5
        self.amenity.number_rooms = 3

    def test_amenity_valid_id(self):
        self.assertIsNotNone(self.amenity.id)
        self.assertEqual(len(self.amenity.id), 36)
        self.assertIsInstance(self.amenity.id, str)

    def test_amenity_valid_created_date(self):
        self.assertIsNotNone(self.amenity.created_at)

    def test_amenity_typeof_created_at(self):
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)

    def test_amenity_valid_updated_date(self):
        self.assertIsNotNone(self.amenity.updated_at)

    def test_amenity_typeof_updated_at(self):
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)

    def test_amenity_save_method(self):
        time_now = datetime.datetime.now()
        self.assertLessEqual(self.amenity.updated_at, time_now)
        self.amenity.save()
        self.assertGreaterEqual(self.amenity.updated_at, time_now)

    def test_amenity_to_dict_method(self):
        d = self.amenity.to_dict()
        self.assertEqual(d['__class__'], "Amenity")

    def test_creating_amenitymodel_obj_from_dictionary(self):
        d = self.amenity.to_dict()
        newobj = Amenity(**d)
        self.assertEqual(d['name'], newobj.name)


if __name__ == '__main__':
    unittest.main()
