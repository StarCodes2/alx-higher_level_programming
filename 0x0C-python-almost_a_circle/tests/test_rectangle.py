#!/usr/bin/python3
"""Defines a test class to test the class Rectangle."""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Define method to test the Rectangle class."""
    def test_inherit(self):
        """Test if Rectangle inherits from Base."""
        a = Rectangle(10, 5, 2, 5)
        self.assertIsInstance(a, Base)
