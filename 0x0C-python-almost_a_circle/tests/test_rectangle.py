#!/usr/bin/python3
"""Defines a test class to test the class Rectangle."""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Define method to test the Rectangle class."""
    def test_inherit(self):
        """Test if Rectangle inherits from Base."""
        a = Rectangle(10, 5, 2, 5)
        self.assertIsInstance(a, Base)

    def test_properties(self):
        """Tests the attributes setters and getters."""
        a = Rectangle(20, 10)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.width, 20)

        a.x = 5
        a.y = 3
        b = Rectangle(20, 10, 5, 3)
        self.assertEqual(a.x, 5)
        self.assertEqual(a.y, 3)
        self.assertEqual(b.id, 6)
        self.assertEqual(b.x, 5)
        self.assertEqual(b.y, 3)

    def test_raises(self):
        """Exceptions are raised when an invalid input is passed to the
        attributes."""
        values = ["20", 10, 5, 3, 89]
        self.assertRaises(TypeError, Rectangle, *values, msg="width must be "
                          "an integer")
        values = [20, "10", 5, 3, 89]
        self.assertRaises(TypeError, Rectangle, *values, msg="height must be "
                          "an integer")

        values = [20, 10, "5", 3, 89]
        self.assertRaises(TypeError, Rectangle, *values, msg="x must be an "
                          "integer")
        values = [20, 10, 5, "3", 89]
        self.assertRaises(TypeError, Rectangle, *values, msg="y must be an "
                          "integer")

        values = [0, 10]
        self.assertRaises(ValueError, Rectangle, *values, msg="width must be"
                          " > 0")
        values = [20, 0]
        self.assertRaises(ValueError, Rectangle, *values, msg="height must be"
                          " > 0")

        values = [-20, 2]
        self.assertRaises(ValueError, Rectangle, *values, msg="width must be "
                          "> 0")
        values = [20, -2]
        self.assertRaises(ValueError, Rectangle, *values, msg="height must be "
                          "> 0")

        values = [20, 10, -5]
        self.assertRaises(ValueError, Rectangle, *value, msg="x must be >= 0")
        values = [20, 10, 5, -3]
        self.assertRaises(ValueError, Rectangle, *value, msg="y must be >= 0")
