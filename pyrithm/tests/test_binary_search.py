#! /usr/bin/env python

import unittest
# https://docs.python.org/3/library/unittest.html
import pyrithm.algorithm.search.binary as bsearch  # Local module to be tested

bsearch = bsearch.BinarySearchIterative  # TODO: Also test the recursive version, later when we have it.

class TestBinarySearch(unittest.TestCase):
    def test_algorithm_search_binary(self):

        # 7 Elements
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (0) @ index None
        ).search(0), None)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (1) @ index 0
        ).search(1), 0)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (2) @ index 1
        ).search(2), 1)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (3) @ index None
        ).search(3), None)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (4) @ index 2
        ).search(4), 2)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (5) @ index 3
        ).search(5), 3)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (6) @ index 4
        ).search(6), 4)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (7) @ index None
        ).search(7), None)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (8) @ index 5
        ).search(8), 5)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (9) @ index 6
        ).search(9), 6)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (10) @ index None
        ).search(10), None)
        #



        # 8 Elements
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (0) @ index None
        ).search(0), None)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (1) @ index 0
        ).search(1), 0)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (2) @ index 1
        ).search(2), 1)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (3) @ index None
        ).search(3), None)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (4) @ index 2
        ).search(4), 2)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (5) @ index 3
        ).search(5), 3)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (6) @ index 4
        ).search(6), 4)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (7) @ index None
        ).search(7), None)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (8) @ index 5
        ).search(8), 5)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (9) @ index 6
        ).search(9), 6)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (10) @ index None
        ).search(10), None)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (11) @ index 7
        ).search(11), 7)
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (12) @ index None
        ).search(12), None)
        #
        


        # 18 Elements
        #
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   8   9  10  11  12  13  14  15  16  17     # Indices
            [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 15, 21, 22, 23, 25, 28, 29, 30, ]  # 18 elements, term (21) @ index 11
        ).search(21), 11)
        #







