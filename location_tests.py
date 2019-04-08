import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

        loc = Location("Los Angeles", 13.2, -130.2)
        self.assertEqual(repr(loc),"Location('Los Angeles', 13.2, -130.2)")
    

    def test_eq(self):
        #is equal
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(Location.__eq__(loc1, loc2))

        #is not equal
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Los Angeles", 13.2, -130.2)
        self.assertFalse(Location.__eq__(loc1, loc2))


    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(35.3, loc.lat)
        self.assertEqual(-120.7, loc.lon)


if __name__ == "__main__":
    unittest.main()
