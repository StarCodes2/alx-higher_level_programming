#!/usr/bin/python3
"""Defines the unittest class for the base class."""
from models.base import Base
import unittest


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
