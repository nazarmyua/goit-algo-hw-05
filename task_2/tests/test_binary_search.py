import unittest

from task_2.src.binary_search import search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.arr = [1.5, 2.3, 3.7, 4.2, 5.9, 6.1, 7.8, 9.4]

    def test_search_existing_element(self):
        iterations, upper_bound = search(self.arr, 4.2)
        self.assertEqual(iterations, 1)
        self.assertEqual(upper_bound, 4.2)

    def test_search_non_existing_element(self):
        iterations, upper_bound = search(self.arr, 4.5)
        self.assertEqual(iterations, 3)
        self.assertEqual(upper_bound, 5.9)

    def test_search_smaller_than_all(self):
        iterations, upper_bound = search(self.arr, 1.0)
        self.assertEqual(iterations, 3)
        self.assertEqual(upper_bound, 1.5)

    def test_search_larger_than_all(self):
        iterations, upper_bound = search(self.arr, 10.0)
        self.assertEqual(iterations, 4)
        self.assertIsNone(upper_bound)
