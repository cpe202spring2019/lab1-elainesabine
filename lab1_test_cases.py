import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # length of list is odd
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        self.assertEqual(max_list_iter([15, 14, 17, 1, -4]), 17)

        # length of list is even
        self.assertEqual(max_list_iter([100, -2, 0, -12]), 100)

        # length of list is 1
        self.assertEqual(max_list_iter([1]), 1)

        # list is empty
        self.assertEqual(max_list_iter([]), None)

        # check for exception
        tlist = None
        with self.assertRaises(ValueError): 
            max_list_iter(tlist)


    def test_reverse_rec(self):
        # length of list is odd
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([15, 14, 17, 1, -4]), [-4, 1, 17, 14, 15])

        # length of list is even
        self.assertEqual(reverse_rec([1, 2, 3, -2]), [-2, 3, 2, 1])

        # length of list is 1
        self.assertEqual(reverse_rec([1]), [1])

        # list is empty
        self.assertEqual(reverse_rec([]), [])

        # check for exception
        with self.assertRaises(ValueError):
            reverse_rec(None)
        

    def test_bin_search(self):
        # target == mid
        int_list = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(4, 0, len(int_list) - 1, int_list), 4)

        int_list = [3, 6, 12, 15, 16]
        self.assertEqual(bin_search(12, 0, len(int_list) - 1, int_list), 2)

        int_list = [1]
        self.assertEqual(bin_search(1, 0, len(int_list) - 1, int_list), 0)

        # target doesn't exist
        int_list = [3, 6, 12, 15, 16]
        self.assertEqual(bin_search(13, 0, len(int_list) - 1, int_list), None)

        # target is greater than mid
        int_list = [3, 6, 12, 15, 16]
        self.assertEqual(bin_search(16, 0, len(int_list) - 1, int_list), 4)

        # target is less than mid
        int_list = [3, 6, 12, 15, 16, 21, 31, 41]
        self.assertEqual(bin_search(6, 0, len(int_list) - 1, int_list), 1)

        # check for exception
        with self.assertRaises(ValueError):
            bin_search(1, 0, 12, None)
        

if __name__ == "__main__":
    unittest.main()

    
