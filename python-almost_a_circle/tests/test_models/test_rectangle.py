#!/usr/bin/python3
"""Test cases for Base"""

import unittest
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Base"""

    def test_basics(self):
        """Doc"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r8 = Rectangle(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 2)
            r12 = Rectangle(1, 0)
            r9 = Rectangle(-1, 2)
            r10 = Rectangle(1, -2)
            r13 = Rectangle(1, 2, -3)
            r14 = Rectangle(1, 2, 3, -4)

        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)
            r5 = Rectangle(1, "2")
            r6 = Rectangle(1, 2, "3")
            r7 = Rectangle(1, 2, 3, "4")

    def test_area(self):
        """Doc"""
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.area(), 8)

    def test__str__(self):
        """Doc"""
        r1 = Rectangle(4, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (1) 0/0 - 4/2\n")

    def test_display(self):
        """Doc"""
        r1 = Rectangle(4, 2)
        r2 = Rectangle(4, 2, 3)
        r3 = Rectangle(4, 2, 3, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(),
                             "####\n####\n")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(),
                             "   ####\n   ####\n")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r3.display()
            self.assertEqual(fake_out.getvalue(),
                             "\n\n   ####\n   ####\n")

    def test_to_dictionary(self):
        """Doc"""
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.to_dictionary(),
                         {'id': 20, 'width': 4, 'height': 2, 'x': 0, 'y': 0})

    def test_update(self):
        """Doc"""
        r1 = Rectangle(4, 2)

        r1.update()
        self.assertEqual(r1.id, 21)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 1)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

        r1.update(89, 1, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r1.update(89, 1, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1.update(**{'id': 89})
        self.assertEqual(r1.id, 89)

        r1.update(**{'id': 89, 'width': 1})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

        r1.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_create(self):
        """Doc"""

        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)

        r1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_save_to_file(self):
        """Doc"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(),
                             '[{"id": 19, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_load_from_file(self):
        """Doc"""
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        from_file = Rectangle.load_from_file()
        self.assertEqual(type(from_file), list)
        self.assertEqual(from_file[0].width, 1)
        self.assertEqual(from_file[0].height, 2)


if __name__ == '__main__':
    unittest.main()
