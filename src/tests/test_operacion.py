# -*- coding= utf-8 -*-
import pytest
import unittest
from tests.operacion import area, sum
from math import pi


class TestArea(unittest.TestCase):
    def test_area(self):
        print("valores permitidos")
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(3), pi * (3 ** 2))

    def test_negativos(self):
        print("Test valores negativos")
        self.assertRaises(ValueError, area, -1)

    def test_tipos(self):
        print("Test de tipos no compatibles")
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, "hola")
        self.assertRaises(TypeError, area, 2 + 3j)

class TestSum(unittest.TestCase):


    def test_sum(self):
        self.assertEqual(sum(2, 5), 7)

@pytest.mark.parametrize(
    "input_x, input_y, expected",
        [
            (5, 1, 6),
            (6, sum(4, 2), 12),
            (sum(19, 1), 15, 35),
            (-7, 10, sum(-7, 10))
        ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected
