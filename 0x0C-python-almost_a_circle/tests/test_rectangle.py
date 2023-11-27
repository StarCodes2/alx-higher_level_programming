#!/usr/bin/python3
"""Defines a test class to test the class Rectangle."""
import os
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


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
        b = Rectangle(20, 10, 5, 3, 50)
        self.assertEqual(a.x, 5)
        self.assertEqual(a.y, 3)
        self.assertEqual(b.id, 50)
        self.assertEqual(b.x, 5)
        self.assertEqual(b.y, 3)

    def test_raises(self):
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

    def test_area(self):
        """Checks if the area returned is correct."""
        d = Rectangle(5, 3)
        self.assertEqual(d.area(), 15)
        d.width = 10
        self.assertEqual(d.area(), 30)

    def test_str(self):
        """Checks if the __str__ method returns the correct output."""
        b = Rectangle(5, 3, 2, 2, 98)
        ret = "[Rectangle] (98) 2/2 - 5/3"
        self.assertEqual(str(b), ret)

    def test_display(self):
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

    def test_to_dictionary(self):
        """Tests the to_dictionary method in the rectangle class."""
        b = Rectangle(5, 6, 0, 0, 201)
        sample = {'id': 201, 'width': 5, 'height': 6, 'x': 0, 'y': 0}
        self.assertEqual(b.to_dictionary(), sample)

    def test_update(self):
        """Tests the update method."""
        b = Rectangle(4, 8, 0, 1, 202)

        b.update(203)
        sample = "[Rectangle] (203) 0/1 - 4/8"
        self.assertEqual(str(b), sample)
        sample = "[Rectangle] (204) 0/1 - 4/8"
        b.update(**{'id': 204})
        self.assertEqual(str(b), sample)

        b.update(203, 5)
        sample = "[Rectangle] (203) 0/1 - 5/8"
        self.assertEqual(str(b), sample)
        sample = "[Rectangle] (204) 0/1 - 6/8"
        b.update(id=204, width=6)
        self.assertEqual(str(b), sample)

        b.update(203, 5, 10)
        sample = "[Rectangle] (203) 0/1 - 5/10"
        self.assertEqual(str(b), sample)
        sample = "[Rectangle] (204) 0/1 - 6/12"
        b.update(id=204, width=6, height=12)
        self.assertEqual(str(b), sample)

        b.update(203, 5, 10, 2)
        sample = "[Rectangle] (203) 2/1 - 5/10"
        self.assertEqual(str(b), sample)
        sample = "[Rectangle] (204) 3/1 - 6/12"
        b.update(id=204, width=6, height=12, x=3)
        self.assertEqual(str(b), sample)

        b.update(203, 5, 10, 2, 3)
        sample = "[Rectangle] (203) 2/3 - 5/10"
        self.assertEqual(str(b), sample)
        sample = "[Rectangle] (204) 3/4 - 6/12"
        b.update(id=204, width=6, height=12, x=3, y=4)
        self.assertEqual(str(b), sample)

    def test_create(self):
        """Tests the class method inherited from the Base class."""
        ins = Rectangle.create(id=30)
        sample = "[Rectangle] (30) 0/0 - 1/1"
        self.assertEqual(str(ins), sample)

        ins = Rectangle.create(id=30, width=2)
        sample = "[Rectangle] (30) 0/0 - 2/1"
        self.assertEqual(str(ins), sample)

        ins = Rectangle.create(id=30, width=2, height=4)
        sample = "[Rectangle] (30) 0/0 - 2/4"
        self.assertEqual(str(ins), sample)

        ins = Rectangle.create(id=30, width=2, height=4, x=1)
        sample = "[Rectangle] (30) 1/0 - 2/4"
        self.assertEqual(str(ins), sample)

        ins = Rectangle.create(id=30, width=2, height=4, x=1, y=2)
        sample = "[Rectangle] (30) 1/2 - 2/4"
        self.assertEqual(str(ins), sample)

    def test_save_to_file(self):
        """Test the class method 'save_to_file' inherited from base class.
        Also tests the 'load_from_file' method."""
        list_obj = Rectangle.load_from_file()
        self.assertTrue(list_obj == [])

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as jf:
            text = jf.read()
        self.assertEqual(text, "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as jf:
            text = jf.read()
        self.assertEqual(text, "[]")

        text = Rectangle.load_from_file()
        self.assertEqual(text, [])

        Rectangle.save_to_file([Rectangle(2, 3, 0, 0, 205)])
        with open("Rectangle.json", "r") as jf:
            text = jf.read()
        self.assertEqual(text, '[{"id": 205,'
                               ' "width": 2, "height": 3, "x": 0, "y": 0}]')

        list_obj = Rectangle.load_from_file()
        self.assertEqual(list_obj[0].id, 205)

        os.remove("Rectangle.json")

if __name__ == "__main__":
    unittest.main()
