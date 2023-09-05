# -*- coding: utf-8 -*-
"""Tests for ``quicktile.layout`` module"""

__author__ = "Jason Graham (jasonisgraham)"
__license__ = "GNU GPL 2.0 or later"

import unittest
from quicktile.layout import (make_winsplit_positions)

class TestMakeWinsplitPositions(unittest.TestCase):
    def test_col_count_only(self):
        actual = make_winsplit_positions(2)

        self.assertEqual(actual['bottom'], [(0.0, 0.5, 1.0, 0.5), (0.25, 0.5, 0.5, 0.5)])
        self.assertEqual(actual['bottom-left'], [(0.0, 0.5, 0.5, 0.5), (0.0, 0.5, 0.5, 0.5)])
        self.assertEqual(actual['bottom-right'], [(0.5, 0.5, 0.5, 0.5), (0.5, 0.5, 0.5, 0.5)])
        self.assertEqual(actual['center'], [(0.0, 0.0, 1.0, 1), (0.25, 0.0, 0.5, 1)])
        self.assertEqual(actual['left'], [(0.0, 0.0, 0.5, 1), (0.0, 0.0, 0.5, 1)])
        self.assertEqual(actual['right'], [(0.5, 0.0, 0.5, 1), (0.5, 0.0, 0.5, 1)])
        self.assertEqual(actual['top'], [(0.0, 0.0, 1.0, 0.5), (0.25, 0.0, 0.5, 0.5)])
        self.assertEqual(actual['top-left'], [(0.0, 0.0, 0.5, 0.5), (0.0, 0.0, 0.5, 0.5)])
        self.assertEqual(actual['top-right'], [(0.5, 0.0, 0.5, 0.5), (0.5, 0.0, 0.5, 0.5)])

    def test_col_count_row_count(self):
        actual = make_winsplit_positions(columns=2, rows=2)

        self.assertEqual(actual['bottom'], [(0.0, 0.5, 1.0, 0.5), (0.25, 0.5, 0.5, 0.5)])
        self.assertEqual(actual['bottom-left'], [(0.0, 0.5, 0.5, 0.5), (0.0, 0.5, 0.5, 0.5)])
        self.assertEqual(actual['bottom-right'], [(0.5, 0.5, 0.5, 0.5), (0.5, 0.5, 0.5, 0.5)])
        self.assertEqual(actual['center'], [(0.0, 0.0, 1.0, 1), (0.25, 0.0, 0.5, 1)])
        self.assertEqual(actual['left'], [(0.0, 0.0, 0.5, 1), (0.0, 0.0, 0.5, 1)])
        self.assertEqual(actual['right'], [(0.5, 0.0, 0.5, 1), (0.5, 0.0, 0.5, 1)])
        self.assertEqual(actual['top'], [(0.0, 0.0, 1.0, 0.5), (0.25, 0.0, 0.5, 0.5)])
        self.assertEqual(actual['top-left'], [(0.0, 0.0, 0.5, 0.5), (0.0, 0.0, 0.5, 0.5)])
        self.assertEqual(actual['top-right'], [(0.5, 0.0, 0.5, 0.5), (0.5, 0.0, 0.5, 0.5)])
