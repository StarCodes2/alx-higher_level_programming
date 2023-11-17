#!/usr/bin/python3
"""Defines a test class to test the class Rectangle."""
from models.base import Base
from models.rectangle import Rectangle
import unittest
from unittest.mock import patch
import io


class TestRectangle(unittest.TestCase):
    """Define method to test the Rectangle class."""
    def test_1inherit(self):
        """Test if Rectangle inherits from Base."""
        a = Rectangle(10, 5, 2, 5)
        self.assertIsInstance(a, Base)

    def test_2properties(self):
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

    def test_3raises(self):
        """Exceptions are raised when an invalid input is passed to the
        attributes."""
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("20", 10)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(20, "10")

        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(20, 10, "5")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(20, 10, 5, "3")

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 10)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(20, 0)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-20, 2)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(20, -2)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(20, 10, -5)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(20, 10, 5, -3)

    def test_4area(self):
        """Checks if the area returned is correct."""
        d = Rectangle(5, 3)
        self.assertEqual(d.area(), 15)
        d.width = 10
        self.assertEqual(d.area(), 30)

    def test_5str(self):
        """Checks if the __str__ method returns the correct output."""
        b = Rectangle(5, 3, 2, 2, 98)
        ret = "[Rectangle] (98) 2/2 - 5/3"
        self.assertEqual(str(b), ret)

    def test_6display(self):
        """Checks if the display method prints the correct output."""
        pri = "##\n##\n##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            b = Rectangle(2, 3, 0, 0)
            b.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, pri)

            pri += "  ##\n  ##\n  ##\n"
            b.x = 2
            b.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, pri)

            pri += "\n  ##\n  ##\n  ##\n"
            b.y = 1
            b.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, pri)

            pri += "\n##\n##\n##\n"
            b.x = 0
            b.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, pri)
