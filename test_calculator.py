import unittest
from calculator import Deal


class CalculatorTests(unittest.TestCase):
    def test_example_max_bid(self):
        self.assertEqual(Deal().max_bid, 6100)

    def test_profit_at_bid(self):
        self.assertEqual(Deal().profit_at_bid(4900), 2700)

    def test_roi(self):
        self.assertAlmostEqual(Deal().roi_at_bid(4900), 2700 / 6800)

    def test_negative_rejected(self):
        with self.assertRaises(ValueError):
            Deal(repairs=-1)


if __name__ == "__main__":
    unittest.main()
