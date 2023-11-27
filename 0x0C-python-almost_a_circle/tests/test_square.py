#!/usr/bin/python3
"""Defines a test class to test the class Square."""
from models.square import Square
from models.rectangle import Rectangle
import unittest
from unittest.mock import patch
import io
import os


class TestSquare(unittest.TestCase):
    """Define method to test the Square class."""
    def test_inherit(self):
        """Test if Square inherits from Base."""
        a = Square(10, 2, 5)
        self.assertIsInstance(a, Rectangle)

    def test_properties(self):
        """Tests the attributes setters and getters."""
        a = Square(20)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.size, 20)

        a.x = 5
        a.y = 3
        b = Square(20, 5, 3, 60)
        self.assertEqual(a.x, 5)
        self.assertEqual(a.y, 3)
        self.assertEqual(b.id, 60)
        self.assertEqual(b.x, 5)
        self.assertEqual(b.y, 3)

    def test_raises(self):
        """Exceptions are raised when an invalid input is passed to the
        attributes."""
        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square("20")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(20, "5")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(20, 5, "3")

        with self.assertRaises(ValueError, msg="size must be > 0"):
            Square(0)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(-20)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Square(20, -5)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Square(20, 5, -3)

    def test_area(self):
        """Checks if the area returned is correct."""
        d = Square(5)
        self.assertEqual(d.area(), 25)
        d.size = 10
        self.assertEqual(d.area(), 100)

    def test_str(self):
        """Checks if the __str__ method returns the correct output."""
        b = Square(5, 2, 2, 98)
        ret = "[Square] (98) 2/2 - 5"
        self.assertEqual(str(b), ret)

    def display(self):
        """Checks if the display method prints the correct output."""
        pri = "##\n##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            b = Square(2, 0, 0)
            b.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, pri)

            pri += "  ##\n  ##\n"
            b.x = 2
            b.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, pri)

            pri += "\n  ##\n  ##\n"
            b.y = 1
            b.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, pri)

            pri += "\n##\n##\n"
            b.x = 0
            b.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, pri)

    def test_to_dictionary(self):
        """Tests the to_dictionary method in the square class."""
        b = Square(5, 0, 0, 301)
        sample = {'id': 301, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(b.to_dictionary(), sample)

    def test_update(self):
        """Tests the update method."""
        b = Square(8, 0, 1, 302)

        b.update(303)
        sample = "[Square] (303) 0/1 - 8"
        self.assertEqual(str(b), sample)
        sample = "[Square] (304) 0/1 - 8"
        b.update(**{'id': 304})
        self.assertEqual(str(b), sample)

        b.update(303, 5)
        sample = "[Square] (303) 0/1 - 5"
        self.assertEqual(str(b), sample)
        sample = "[Square] (304) 0/1 - 6"
        b.update(id=304, size=6)
        self.assertEqual(str(b), sample)

        b.update(303, 5, 2)
        sample = "[Square] (303) 2/1 - 5"
        self.assertEqual(str(b), sample)
        sample = "[Square] (304) 3/1 - 6"
        b.update(id=304, size=6, x=3)
        self.assertEqual(str(b), sample)

        b.update(303, 5, 2, 3)
        sample = "[Square] (303) 2/3 - 5"
        self.assertEqual(str(b), sample)
        sample = "[Square] (304) 3/4 - 6"
        b.update(id=304, size=6, x=3, y=4)
        self.assertEqual(str(b), sample)

    def test_create(self):
        """Tests the class method inherited from the Rectangle class."""
        ins = Square.create(id=40)
        sample = "[Square] (40) 0/0 - 1"
        self.assertEqual(str(ins), sample)

        ins = Square.create(id=40, size=2)
        sample = "[Square] (40) 0/0 - 2"
        self.assertEqual(str(ins), sample)

        ins = Square.create(id=40, size=2, x=1)
        sample = "[Square] (40) 1/0 - 2"
        self.assertEqual(str(ins), sample)

        ins = Square.create(id=40, size=2, x=1, y=2)
        sample = "[Square] (40) 1/2 - 2"
        self.assertEqual(str(ins), sample)

    def test_save_to_file(self):
        """Test the class method 'save_to_file' inherited from base class.
        Also tests the 'load_from_file' method."""
        file_name = "Square.json"

        """testing the load_from_file method whnen file does not exist."""
        list_obj = Square.load_from_file()
        self.assertTrue(list_obj == [])

        Square.save_to_file(None)
        with open(file_name, "r") as jf:
            text = jf.read()
        self.assertEqual(text, "[]")

        Square.save_to_file([])
        with open(file_name, "r") as jf:
            text = jf.read()
        self.assertEqual(text, "[]")

        """Testing the load_from_file method."""
        text = Square.load_from_file()
        self.assertEqual(text, [])

        Square.save_to_file([Square(2, 0, 0, 305)])
        with open(file_name, "r") as jf:
            text = jf.read()
        self.assertEqual(text, '[{"id": 305, "size": 2, "x": 0, "y": 0}]')

        """Testing that the load_from_file method returns a list of objects"""
        list_obj = Square.load_from_file()
        self.assertEqual(list_obj[0].id, 305)

        """Deletes the json file created by this tests:"""
        os.remove(file_name)

if __name__ == "__main__":
    unittest.main()
