#!/usr/bin/python3
import unittest
from models.state import State
from uuid import uuid4
import datetime
"""unittest for state class
"""


class TestState(unittest.TestCase):
    """ class for testing state Class """

    def setUp(self):
        self.state = State()
        self.state.name = "New orliens"

    def test_state_valid_id(self):
        self.assertIsNotNone(self.state.id)
        self.assertEqual(len(self.state.id), 36)
        self.assertIsInstance(self.state.id, str)

    def test_state_valid_created_date(self):
        self.assertIsNotNone(self.state.created_at)

    def test_state_typeof_created_at(self):
        self.assertIsInstance(self.state.created_at, datetime.datetime)

    def test_state_valid_updated_date(self):
        self.assertIsNotNone(self.state.updated_at)

    def test_state_typeof_updated_at(self):
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

    def test_state_save_method(self):
        time_now = datetime.datetime.now()
        self.assertLessEqual(self.state.updated_at, time_now)
        self.state.save()
        self.assertGreaterEqual(self.state.updated_at, time_now)

    def test_state_to_dict_method(self):
        d = self.state.to_dict()
        self.assertEqual(d['__class__'], "State")

    def test_creating_statemodel_obj_from_dictionary(self):
        d = self.state.to_dict()
        newobj = State(**d)
        self.assertEqual(d['name'], newobj.name)


if __name__ == '__main__':
    unittest.main()
