import unittest
from circle_calc import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self) -> None:
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(TypeError, circle_area, "John")
