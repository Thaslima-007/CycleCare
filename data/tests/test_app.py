import unittest
from datetime import date, timedelta


def estimate_next_period(last_period, cycle_length):
    if not 21 <= cycle_length <= 45:
        raise ValueError("Cycle length must be between 21 and 45 days")
    return last_period + timedelta(days=cycle_length)


class TestCycleCare(unittest.TestCase):

    def test_28_day_cycle(self):
        result = estimate_next_period(date(2026, 1, 1), 28)
        self.assertEqual(result, date(2026, 1, 29))

    def test_30_day_cycle(self):
        result = estimate_next_period(date(2026, 1, 1), 30)
        self.assertEqual(result, date(2026, 1, 31))

    def test_short_cycle_rejected(self):
        with self.assertRaises(ValueError):
            estimate_next_period(date(2026, 1, 1), 15)

    def test_long_cycle_rejected(self):
        with self.assertRaises(ValueError):
            estimate_next_period(date(2026, 1, 1), 50)


if __name__ == "__main__":
    unittest.main()
