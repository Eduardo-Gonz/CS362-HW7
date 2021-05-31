import unittest
import leap


class TestLeapYear(unittest.TestCase):
    def test_input(self):
        self.assertEqual(leap.is_leap_year(1995), "1995 is not a leap year!")
        self.assertEqual(leap.is_leap_year(1996), "1996 is a leap year!")




if __name__ == "__main__":
    unittest.main()