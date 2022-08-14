#!/usr/bin/python3
""""Doc"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """"Doc"""

    def test_simple_case(self):
        """"Doc"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_case(self):
        """"Doc"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_case(self):
        """"Doc"""
        self.assertEqual(max_integer([]), None)
