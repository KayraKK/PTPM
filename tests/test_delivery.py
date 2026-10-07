import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from delivery_service import calculate_delivery_cost


class TestDelivery(unittest.TestCase):

    def test_ves_menshe_minimuma(self):
        cost, _ = calculate_delivery_cost(0.05, 100, "обычный")
        self.assertEqual(cost, -1)

    def test_ves_bolshe_maksimuma(self):
        cost, _ = calculate_delivery_cost(51.0, 100, "обычный")
        self.assertEqual(cost, -1)

    def test_rasstoyanie_nol(self):
        cost, _ = calculate_delivery_cost(1.0, 0, "обычный")
        self.assertEqual(cost, -1)

    def test_rasstoyanie_bolshe_maksimuma(self):
        cost, _ = calculate_delivery_cost(1.0, 5001, "обычный")
        self.assertEqual(cost, -1)

    def test_neizvestnyy_tip(self):
        cost, _ = calculate_delivery_cost(1.0, 100, "какой-то")
        self.assertEqual(cost, -1)

    def test_bazovaya_stoimost(self):
        # 200 + 100*5 = 700
        cost, _ = calculate_delivery_cost(1.0, 100, "обычный")
        self.assertEqual(cost, 700)

    def test_ves_5_bez_mnozhitelya(self):
        # вес=5 → не >5 → без множителя. 200 + 200*5 = 1200
        cost, _ = calculate_delivery_cost(5.0, 200, "обычный")
        self.assertEqual(cost, 1200)

    def test_ves_10_mnozhitel_1_2(self):
        # 700 * 1.2 = 840
        cost, _ = calculate_delivery_cost(10.0, 100, "обычный")
        self.assertEqual(cost, 840)

    def test_ves_20_mnozhitel_1_5(self):
        # 700 * 1.5 = 1050
        cost, _ = calculate_delivery_cost(20.0, 100, "обычный")
        self.assertEqual(cost, 1050)

    def test_hrupkiy_plus_300(self):
        # 700 + 300 = 1000
        cost, _ = calculate_delivery_cost(1.0, 100, "хрупкий")
        self.assertEqual(cost, 1000)

    def test_opasnyy_plus_1000(self):
        # 700 + 1000 = 1700
        cost, _ = calculate_delivery_cost(1.0, 100, "опасный")
        self.assertEqual(cost, 1700)

    def test_express_dorozhe_obychnogo(self):
        # БАГ: экспресс должен быть дороже, а в коде *= 0.5
        regular, _ = calculate_delivery_cost(1.0, 100, "обычный", False)
        express, _ = calculate_delivery_cost(1.0, 100, "обычный", True)
        self.assertGreater(express, regular)


if __name__ == "__main__":
    unittest.main()