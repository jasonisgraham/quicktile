# -*- coding: utf-8 -*-
"""Tests for ``quicktile.layout`` module"""

__author__ = "Jason Graham (jasonisgraham)"
__license__ = "GNU GPL 2.0 or later"

import unittest
from quicktile.layout import (make_winsplit_positions)


class TestMakeWinsplitPositions(unittest.TestCase):
    def test_col_count_only(self):
        actual = make_winsplit_positions(3)

        self.assertEqual(actual['center'], [(0.0, 0.0, 1.0, 1), (0.334, 0.0, 0.333, 1), (0.166, 0.0, 0.667, 1)]),
        self.assertEqual(actual['left'], [(0.0, 0.0, 0.5, 1), (0.0, 0.0, 0.333, 1), (0.0, 0.0, 0.667, 1)])
        self.assertEqual(actual['right'], [(0.5, 0.0, 0.5, 1), (0.667, 0.0, 0.333, 1), (0.333, 0.0, 0.667, 1)])
        self.assertEqual(actual['bottom'], [(0.0, 0.5, 1.0, 0.5), (0.334, 0.5, 0.333, 0.5), (0.166, 0.5, 0.667, 0.5)])
        self.assertEqual(actual['bottom-left'], [(0.0, 0.5, 0.5, 0.5), (0.0, 0.5, 0.333, 0.5), (0.0, 0.5, 0.667, 0.5)])
        self.assertEqual(actual['bottom-right'],
                         [(0.5, 0.5, 0.5, 0.5), (0.667, 0.5, 0.333, 0.5), (0.333, 0.5, 0.667, 0.5)])
        self.assertEqual(actual['top'], [(0.0, 0.0, 1.0, 0.5), (0.334, 0.0, 0.333, 0.5), (0.166, 0.0, 0.667, 0.5)])
        self.assertEqual(actual['top-left'], [(0.0, 0.0, 0.5, 0.5), (0.0, 0.0, 0.333, 0.5), (0.0, 0.0, 0.667, 0.5)])
        self.assertEqual(actual['top-right'],
                         [(0.5, 0.0, 0.5, 0.5), (0.667, 0.0, 0.333, 0.5), (0.333, 0.0, 0.667, 0.5)])

    def fuzzy_equal(self, actual, exp, msg):
        round_to = 2
        self.assertEqual(list(map(lambda x: round(x, round_to), actual)),
                         list(map(lambda x: round(x, round_to), exp)),
                         msg)

    def test_col_count_row_count_equal_3_cycle_both_rows_and_columns(self):
        actual = make_winsplit_positions(columns=3, rows=3)

        # unchanged
        self.assertEqual(actual['center'], [(0.0, 0.0, 1.0, 1), (0.334, 0.0, 0.333, 1), (0.166, 0.0, 0.667, 1)]),
        self.assertEqual(actual['left'], [(0.0, 0.0, 0.5, 1), (0.0, 0.0, 0.333, 1), (0.0, 0.0, 0.667, 1)])
        self.assertEqual(actual['right'], [(0.5, 0.0, 0.5, 1), (0.667, 0.0, 0.333, 1), (0.333, 0.0, 0.667, 1)])
        self.assertEqual(actual['bottom'], [(0.0, 0.5, 1.0, 0.5), (0.334, 0.5, 0.333, 0.5), (0.166, 0.5, 0.667, 0.5)])
        self.assertEqual(actual['bottom-left'], [(0.0, 0.5, 0.5, 0.5), (0.0, 0.5, 0.333, 0.5), (0.0, 0.5, 0.667, 0.5)])
        self.assertEqual(actual['bottom-right'],
                         [(0.5, 0.5, 0.5, 0.5), (0.667, 0.5, 0.333, 0.5), (0.333, 0.5, 0.667, 0.5)])
        self.assertEqual(actual['top'], [(0.0, 0.0, 1.0, 0.5), (0.334, 0.0, 0.333, 0.5), (0.166, 0.0, 0.667, 0.5)])
        self.assertEqual(actual['top-left'], [(0.0, 0.0, 0.5, 0.5), (0.0, 0.0, 0.333, 0.5), (0.0, 0.0, 0.667, 0.5)])
        self.assertEqual(actual['top-right'],
                         [(0.5, 0.0, 0.5, 0.5), (0.667, 0.0, 0.333, 0.5), (0.333, 0.0, 0.667, 0.5)])
        self.assertEqual(actual['center'], [(0.0, 0.0, 1.0, 1), (0.334, 0.0, 0.333, 1), (0.166, 0.0, 0.667, 1)]),
        self.assertEqual(actual['left'], [(0.0, 0.0, 0.5, 1), (0.0, 0.0, 0.333, 1), (0.0, 0.0, 0.667, 1)])
        self.assertEqual(actual['right'], [(0.5, 0.0, 0.5, 1), (0.667, 0.0, 0.333, 1), (0.333, 0.0, 0.667, 1)])
        self.assertEqual(actual['bottom'], [(0.0, 0.5, 1.0, 0.5), (0.334, 0.5, 0.333, 0.5), (0.166, 0.5, 0.667, 0.5)])

        # affected
        bottom = actual['bottom-fill']
        self.fuzzy_equal(bottom[0], (0.0, 0.5, 1, 1.0 / 2), "fill bottom half of screen")
        self.fuzzy_equal(bottom[1], (0.0, 2.0 / 3, 1, 1.0 / 3), "fill bottom 1/3 of screen")
        self.fuzzy_equal(bottom[2], (0.0, 1.0 / 3, 1, 2.0 / 3), "fill bottom 2/3 of screen")

        top = actual['top-fill']
        self.fuzzy_equal(top[0], (0.0, 0.5, 1, 1.0 / 3), "fill top half of screen")
        self.fuzzy_equal(top[1], (0.0, 2.0 / 3, 1, 1.0 / 3), "fill top 1/3 of screen")
        self.fuzzy_equal(top[2], (0.0, 1.0 / 3, 1, 2.0 / 3), "fill top 2/3 of screen")
