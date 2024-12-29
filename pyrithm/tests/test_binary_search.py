#! /usr/bin/env python

import unittest
# https://docs.python.org/3/library/unittest.html
import pyrithm.algorithm.search.binary as bsearch  # Local module to be tested

bsearch = bsearch.BinarySearchIterative  # TODO: Also test the recursive version, later when we have it.

class TestBinarySearch(unittest.TestCase):

    # 1 Element Tests

    def test_algorithm_search_binary__1e_t0_iN(self):
        self.assertEqual(bsearch(
            #0   # Indices
            [1, ]  # 1 element, term (0) @ index None
        ).search(0), None)

    def test_algorithm_search_binary__1e_t1_i0(self):
        self.assertEqual(bsearch(
            #0   # Indices
            [1, ]  # 1 element, term (1) @ index 0
        ).search(1), 0)


    # 2 Element Tests

    def test_algorithm_search_binary__2e_t0_iN(self):
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (0) @ index None
        ).search(0), None)

    def test_algorithm_search_binary__2e_t1_i0(self):
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (1) @ index 0
        ).search(1), 0)

    def test_algorithm_search_binary__2e_t2_i1(self):
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (2) @ index 1
        ).search(2), 1)

    # THIS IS THE EDGE CASE FAILING WITH "list index out of range".
    # UNIQUE FACTORS: The term is not in the list and is >> last element. It is a 2 element list and this means that
    # the mid index will fall on min or max. NOW, for solution, focusing on how in the case of 2 elements, the // 2
    # integer division results in the mid_index == max_index and so the left side has one element and the right side has none.
    # SOLUTION ??? I don't know yet.
    def test_algorithm_search_binary__2e_t3_iN(self):
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (3) @ index None
        ).search(3), None)


    # 3 Element Tests

    def test_algorithm_search_binary__3e_t0_iN(self):
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (0) @ index None
        ).search(0), None)

    def test_algorithm_search_binary__3e_t1_i0(self):
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (1) @ index 0
        ).search(1), 0)

    def test_algorithm_search_binary__3e_t2_i1(self):
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (2) @ index 1
        ).search(2), 1)

    def test_algorithm_search_binary__3e_t3_iN(self):
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (3) @ index None
        ).search(3), None)

    def test_algorithm_search_binary__3e_t4_i2(self):
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (4) @ index 2
        ).search(4), 2)

    def test_algorithm_search_binary__3e_t5_iN(self):
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (5) @ index None
        ).search(5), None)


    # TODO: 4 Element Tests, 5 Element Tests, 6 Element Tests


    # 7 Element Tests

    def test_algorithm_search_binary__7e_t0_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (0) @ index None
        ).search(0), None)


    # 7 Element Tests

    def test_algorithm_search_binary__7e_t0_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (0) @ index None
        ).search(0), None)

    def test_algorithm_search_binary__7e_t1_i0(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (1) @ index 0
        ).search(1), 0)

    def test_algorithm_search_binary__7e_t2_i1(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (2) @ index 1
        ).search(2), 1)

    def test_algorithm_search_binary__7e_t3_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (3) @ index None
        ).search(3), None)

    def test_algorithm_search_binary__7e_t4_i2(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (4) @ index 2
        ).search(4), 2)

    def test_algorithm_search_binary__7e_t5_i3(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (5) @ index 3
        ).search(5), 3)

    def test_algorithm_search_binary__7e_t6_i4(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (6) @ index 4
        ).search(6), 4)

    def test_algorithm_search_binary__7e_t7_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (7) @ index None
        ).search(7), None)

    def test_algorithm_search_binary__7e_t8_i5(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (8) @ index 5
        ).search(8), 5)

    def test_algorithm_search_binary__7e_t9_i6(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (9) @ index 6
        ).search(9), 6)

    def test_algorithm_search_binary__7e_t10_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   # Indices
            [1, 2, 4, 5, 6, 8, 9, ]  # 7 elements, term (10) @ index None
        ).search(10), None)


    # 8 Element Tests

    def test_algorithm_search_binary__8e_t0_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (0) @ index None
        ).search(0), None)

    def test_algorithm_search_binary__8e_t1_i0(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (1) @ index 0
        ).search(1), 0)

    def test_algorithm_search_binary__8e_t2_i1(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (2) @ index 1
        ).search(2), 1)

    def test_algorithm_search_binary__8e_t3_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (3) @ index None
        ).search(3), None)

    def test_algorithm_search_binary__8e_t4_i2(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (4) @ index 2
        ).search(4), 2)

    def test_algorithm_search_binary__8e_t5_i3(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (5) @ index 3
        ).search(5), 3)

    def test_algorithm_search_binary__8e_t6_i4(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (6) @ index 4
        ).search(6), 4)

    def test_algorithm_search_binary__8e_t7_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (7) @ index None
        ).search(7), None)

    def test_algorithm_search_binary__8e_t8_i5(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (8) @ index 5
        ).search(8), 5)

    def test_algorithm_search_binary__8e_t9_i6(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (9) @ index 6
        ).search(9), 6)

    def test_algorithm_search_binary__8e_t10_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (10) @ index None
        ).search(10), None)

    def test_algorithm_search_binary__8e_t11_i7(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (11) @ index 7
        ).search(11), 7)

    def test_algorithm_search_binary__8e_t12_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6   7   # Indices
            [1, 2, 4, 5, 6, 8, 9, 11, ]  # 8 elements, term (12) @ index None
        ).search(12), None)


    # High Element Tests

    def test_algorithm_search_binary__18e_t21_i11(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   8   9  10  11  12  13  14  15  16  17     # Indices
            [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 15, 21, 22, 23, 25, 28, 29, 30, ]  # 18 elements, term (21) @ index 11
        ).search(21), 11)
        #


##
#

