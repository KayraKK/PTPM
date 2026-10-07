import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from my_project import triangle, parse_and_solve


class TestTriangle(unittest.TestCase):

    def test_ravnostoronniy(self):
        t, _ = triangle(5, 5, 5)
        self.assertEqual(t, "равносторонний")

    def test_ravnobedrenniy_ab(self):
        t, _ = triangle(5, 5, 6)
        self.assertEqual(t, "равнобедренный")

    def test_ravnobedrenniy_ac(self):
        t, _ = triangle(5, 6, 5)
        self.assertEqual(t, "равнобедренный")

    def test_ravnobedrenniy_bc(self):
        t, _ = triangle(6, 5, 5)
        self.assertEqual(t, "равнобедренный")

    def test_raznostoronniy(self):
        t, _ = triangle(3, 4, 5)
        self.assertEqual(t, "разносторонний")

    def test_summa_ravna_tretey(self):
        t, _ = triangle(1, 2, 3)
        self.assertEqual(t, "не треугольник")

    def test_summa_menshe_tretey(self):
        t, _ = triangle(1, 2, 10)
        self.assertEqual(t, "не треугольник")

    def test_nol(self):
        t, _ = triangle(0, 5, 5)
        self.assertEqual(t, "не треугольник")

    def test_minus(self):
        t, _ = triangle(-3, 4, 5)
        self.assertEqual(t, "не треугольник")

    def test_koordinaty_net_treugolnika(self):
        _, coords = triangle(1, 2, 10)
        self.assertEqual(coords, [(-1, -1)] * 3)

    def test_nekorrektnye_dannye(self):
        t, coords = parse_and_solve("abc", "4", "5")
        self.assertEqual(t, "")
        self.assertEqual(coords, [(-2, -2)] * 3)

    def test_tri_tochki_v_pole(self):
        _, coords = triangle(3, 4, 5)
        self.assertEqual(len(coords), 3)
        for x, y in coords:
            self.assertTrue(0 <= x <= 100 and 0 <= y <= 100)


if __name__ == "__main__":
    unittest.main()