#!/usr/bin/python3
import unittest
from models.review import Review
from uuid import uuid4
import datetime
"""unittest for review class
"""


class TestReview(unittest.TestCase):
    """ class for testing review Class """

    def setUp(self):
        self.review = Review()
        self.review.name = "New orliens"

    def test_review_valid_id(self):
        self.assertIsNotNone(self.review.id)
        self.assertEqual(len(self.review.id), 36)
        self.assertIsInstance(self.review.id, str)

    def test_review_valid_created_date(self):
        self.assertIsNotNone(self.review.created_at)

    def test_review_typeof_created_at(self):
        self.assertIsInstance(self.review.created_at, datetime.datetime)

    def test_review_valid_updated_date(self):
        self.assertIsNotNone(self.review.updated_at)

    def test_review_typeof_updated_at(self):
        self.assertIsInstance(self.review.updated_at, datetime.datetime)

    def test_review_save_method(self):
        time_now = datetime.datetime.now()
        self.assertLessEqual(self.review.updated_at, time_now)
        self.review.save()
        self.assertGreaterEqual(self.review.updated_at, time_now)

    def test_review_to_dict_method(self):
        d = self.review.to_dict()
        self.assertEqual(d['__class__'], "Review")

    def test_creating_reviewmodel_obj_from_dictionary(self):
        d = self.review.to_dict()
        newobj = Review(**d)
        self.assertEqual(d['name'], newobj.name)


if __name__ == '__main__':
    unittest.main()
