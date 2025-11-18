import unittest
import lib.circle as circle
import lib.rectangle as rectangle
import lib.square as square
import math


class RectUnitTests(unittest.TestCase):
    def test_area_simple(self):
        area = rectangle.area(3, 5)
        self.assertEqual(area, 15)

    def test_area_square(self):
        area = rectangle.area(2, 2)
        self.assertEqual(area, 4)

    def test_area_zero_side(self):
        area = rectangle.area(2, 0)
        self.assertEqual(area, 0)

    def test_area_both_sides_zero(self):
        area = rectangle.area(0, 0)
        self.assertEqual(area, 0)

    def test_area_neg_side(self):
        area = rectangle.area(-5, 2)
        self.assertEqual(area, -10)

    def test_perim_gold(self):
        phi = (5**0.5 - 1) / 2
        perim = rectangle.perimeter(1, phi)
        self.assertAlmostEqual(perim, 5**0.5 + 1)

    def test_perim_square(self):
        perim = rectangle.perimeter(1, 5)
        self.assertAlmostEqual(perim, 12)

    def test_perim_neg_side(self):
        perim = rectangle.perimeter(1, -1)
        self.assertAlmostEqual(perim, 0)


class CircleUnitTests(unittest.TestCase):
    def test_area_simple(self):
        area = circle.area(3)
        self.assertAlmostEqual(area, math.pi * 9)

    def test_area_zero(self):
        area = circle.area(0)
        self.assertEqual(area, 0)

    def test_area_neg(self):
        area = circle.area(-2)
        self.assertAlmostEqual(area, math.pi * 4)

    def test_perim_one(self):
        perim = circle.perimeter(1)
        self.assertAlmostEqual(perim, 2 * math.pi)

    def test_perim_zero(self):
        perim = circle.perimeter(0)
        self.assertEqual(perim, 0)

    def test_perim_neg(self):
        perim = circle.perimeter(-5)
        self.assertAlmostEqual(perim, math.pi * -10)


class SquareUnitTests(unittest.TestCase):
    def test_area_1(self):
        area = square.area(1)
        self.assertEqual(area, 1)

    def test_area_zero(self):
        area = square.area(0)
        self.assertEqual(area, 0)

    def test_area_neg(self):
        area = square.area(-6)
        self.assertEqual(area, 36)

    def test_area_large(self):
        area = square.area(6398569456956)
        self.assertAlmostEqual(area, 40941691095490200736785936)

    def test_perim_pi(self):
        perim = square.perimeter(math.pi)
        self.assertAlmostEqual(perim, 4 * math.pi)

    def test_perim_neg(self):
        perim = square.perimeter(-7)
        self.assertEqual(perim, -28)

    def test_perim_zero(self):
        perim = square.perimeter(0)
        self.assertEqual(perim, 0)
