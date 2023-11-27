#!/usr/bin/python3
"""Defines the unittest class for the base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines a series of test functions that tests the Base class."""
    def test_id(self):
        """Tests that the base class assigns the right value to the instance
        attribute: id."""
        a = Base()
        b = Base(12)
        c = Base()
        self.assertEqual(b.id, 12)
        self.assertEqual(c.id, 2)
        self.assertEqual(a.id, 1)

    def test_type(self):
        """Tests that the instances are of the same type."""
        a = Base()
        b = Base(12)
        self.assertEqual(type(a), type(b))

    def test_to_json(self):
        """Tests the to_json_string method."""
        jlist = Base.to_json_string(None)
        self.assertEqual(jlist, '[]')

        jlist = Base.to_json_string([])
        self.assertEqual(jlist, '[]')

        jlist = Base.to_json_string([{'id': 20}])
        self.assertEqual(jlist, '[{"id": 20}]')

    def test_from_json(self):
        """Tests the from_json_string method."""
        lists = Base.from_json_string(None)
        self.assertEqual(lists, [])

        lists = Base.from_json_string('[]')
        self.assertEqual(lists, [])

        lists = Base.from_json_string('[{"id": 50}]')
        self.assertEqual(lists, [{'id': 50}])

if __name__ == "__main__":
    unittest.main()
