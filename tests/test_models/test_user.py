#!/usr/bin/python3
import unittest
from models.user import User
from uuid import uuid4
import datetime
"""unittest for user class
"""


class TestUser(unittest.TestCase):
    """ class for testing User Class """

    def setUp(self):
        self.user = User()
        self.user.user_email = "ammar@wpkama.com"
        self.user.password = "123"
        self.user.first_name = "Ammar"

    def test_user_valid_id(self):
        self.assertIsNotNone(self.user.id)
        self.assertEqual(len(self.user.id), 36)
        self.assertIsInstance(self.user.id, str)

    def test_user_valid_created_date(self):
        self.assertIsNotNone(self.user.created_at)

    def test_user_typeof_created_at(self):
        self.assertIsInstance(self.user.created_at, datetime.datetime)

    def test_user_valid_updated_date(self):
        self.assertIsNotNone(self.user.updated_at)

    def test_user_typeof_updated_at(self):
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_user_save_method(self):
        time_now = datetime.datetime.now()
        self.assertLessEqual(self.user.updated_at, time_now)
        self.user.save()
        self.assertGreaterEqual(self.user.updated_at, time_now)

    def test_user_to_dict_method(self):
        d = self.user.to_dict()
        self.assertEqual(d['__class__'], "User")

    def test_creating_usermodel_obj_from_dictionary(self):
        d = self.user.to_dict()
        newobj = User(**d)
        self.assertEqual(d['first_name'], newobj.first_name)
        self.assertEqual(d['user_email'], newobj.user_email)
        self.assertEqual(d['password'], newobj.password)


if __name__ == '__main__':
    unittest.main()
