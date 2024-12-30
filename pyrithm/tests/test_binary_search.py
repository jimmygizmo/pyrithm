#! /usr/bin/env python

import unittest
# https://docs.python.org/3/library/unittest.html

import inspect  # So we can inspect the stack and determine the name of each function for helpful logging.

import pyrithm.algorithm.search.binary as bsearch  # Local module to be tested


V_ = True  # Verbose logging switch

bsearch = bsearch.BinarySearchIterative  # TODO: Also test the recursive version, later when we have it.

# NOTE REGARDING:     inspect.stack()[0][3]
# This is a trick to see the name of the function/test in a convenient manner. I also use configurable verbose
# output from the module iteself and this technique intersperses that output with the descriptive test names. Of
# course part of the value with all this comes from using good, descriptive test names. In my case, these test
# function names are also hierarchically accurate.

# SIDENOTE: If you want to see the functions CALLER:
# inspect.stack()[1][3]
# If we try to implement this more cleanly using a decorator, we might need this.
# TODO: Try implementing these before and after agnostic prints as a decorator. It is a classic use case, but with
# the added complexity of the inspect call needed to see the inner function, not the decorator wrapper function.
# It might just work, or we might need to use the caller version, or this idea might not even work. If it does, it will
# remove a LOT of repeated text from this file, so it would be nice to do.

# Utility function in module space (not in the class). This is a decorator. TODO: Any reason to make it a class func?
def function_headline(decorated_function):
    """For helping unit tests show their names, show function name with ascii header and footer."""
    def wrapper(*args, **kwargs):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[1][3]}")
        result = decorated_function(*args, **kwargs)
        if V_: print(f"- - - - - - - - - - - - - - - -")
        return result
    return wrapper

# TODO: UPDATE: The decorator idea is not working well with inspect but was worth a try and fun. This is what we get:
# inspect.stack()[0][3]    says the function name is 'wrapper'
# inspect.stack()[1][3]    sasys the funtion name is '_callTestMethod'
# This makes sense .. of course we must be INSIDE the function to inspect it and decorators WRAP functions,
# they don' infiltrate them. So this might not ever work with a decorator and it is not a critical feature. But there
# might be some other way to look into later. Alas, this is all because the unittest module does not offer great
# logging or verbosity options for excatly what I want to do in this case.


class TestBinarySearch(unittest.TestCase):

    # 1 Element Tests

    def test_algorithm_search_binary__1e_tM1_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0   # Indices
            [1, ]  # 1 element, term (-1) @ index None
        ).search(-1), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__1e_t0_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0   # Indices
            [1, ]  # 1 element, term (0) @ index None
        ).search(0), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__1e_t1_i0(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0   # Indices
            [1, ]  # 1 element, term (1) @ index 0
        ).search(1), 0)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__1e_t2_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0   # Indices
            [1, ]  # 1 element, term (2) @ index None
        ).search(2), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")


    # 2 Element Tests

    def test_algorithm_search_binary__2e_tM1_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (-1) @ index None
        ).search(-1), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__2e_t0_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (0) @ index None
        ).search(0), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__2e_t1_i0(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (1) @ index 0
        ).search(1), 0)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__2e_t2_i1(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (2) @ index 1
        ).search(2), 1)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__2e_t3_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1   # Indices
            [1, 2, ]  # 2 elements, term (3) @ index None
        ).search(3), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")


    # 3 Element Tests

    def test_algorithm_search_binary__3e_t0_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (0) @ index None
        ).search(0), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__3e_t1_i0(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (1) @ index 0
        ).search(1), 0)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__3e_t2_i1(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (2) @ index 1
        ).search(2), 1)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__3e_t3_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (3) @ index None
        ).search(3), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__3e_t4_i2(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (4) @ index 2
        ).search(4), 2)
        if V_: print(f"- - - - - - - - - - - - - - - -")

    def test_algorithm_search_binary__3e_t5_iN(self):
        if V_: print(f"\n- - - - - - - - - - - - - - - -  UNIT TEST: {inspect.stack()[0][3]}")
        self.assertEqual(bsearch(
            #0  1  2   # Indices
            [1, 2, 4, ]  # 3 elements, term (5) @ index None
        ).search(5), None)
        if V_: print(f"- - - - - - - - - - - - - - - -")


    # 4 Element Tests

    def test_algorithm_search_binary__4e_t0_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3   # Indices
            [1, 2, 4, 5, ]  # 4 elements, term (0) @ index None
        ).search(0), None)

    def test_algorithm_search_binary__4e_t1_i0(self):
        self.assertEqual(bsearch(
            #0  1  2  3   # Indices
            [1, 2, 4, 5, ]  # 4 elements, term (1) @ index 0
        ).search(1), 0)

    def test_algorithm_search_binary__4e_t2_i1(self):
        self.assertEqual(bsearch(
            #0  1  2  3   # Indices
            [1, 2, 4, 5, ]  # 4 elements, term (2) @ index 1
        ).search(2), 1)

    def test_algorithm_search_binary__4e_t3_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3   # Indices
            [1, 2, 4, 5, ]  # 4 elements, term (3) @ index None
        ).search(3), None)

    def test_algorithm_search_binary__4e_t4_i2(self):
        self.assertEqual(bsearch(
            #0  1  2  3   # Indices
            [1, 2, 4, 5, ]  # 4 elements, term (4) @ index 2
        ).search(4), 2)

    def test_algorithm_search_binary__4e_t5_i3(self):
        self.assertEqual(bsearch(
            #0  1  2  3   # Indices
            [1, 2, 4, 5, ]  # 4 elements, term (5) @ index 3
        ).search(5), 3)

    def test_algorithm_search_binary__4e_t6_iN(self):
        self.assertEqual(bsearch(
            #0  1  2  3   # Indices
            [1, 2, 4, 5, ]  # 4 elements, term (6) @ index None
        ).search(6), None)


    # TODO: 5 Element Tests, 6 Element Tests


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



    # Full Sequence Checks - 8 Elements: For finds and misses at all indexes
    # For each position, tries all finds. Then tries all misses including before list and after list misses.

    def test_algorithm_search_binary__8e_find0(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (1) @ index 0
        ).search(1), 0)

    def test_algorithm_search_binary__8e_find1(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (2) @ index 1
        ).search(2), 1)

    def test_algorithm_search_binary__8e_find2(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (3) @ index 2
        ).search(3), 2)

    def test_algorithm_search_binary__8e_find3(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (4) @ index 3
        ).search(4), 3)

    def test_algorithm_search_binary__8e_find4(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (5) @ index 4
        ).search(5), 4)

    def test_algorithm_search_binary__8e_find5(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (6) @ index 5
        ).search(6), 5)

    def test_algorithm_search_binary__8e_find6(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (7) @ index 6
        ).search(7), 6)

    def test_algorithm_search_binary__8e_find7(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (8) @ index 7
        ).search(8), 7)


    # 8 Elements - All misses with before, after misses. (These tests do in fact cover important code/traversal paths.)
    # For the misses, the basic element pattern of 1, 2, 3, 4, 5, 6, 7, 8  is used to create the missing elements with
    # help from the value 0, creating a gap which we move along from left to right for all these full-span miss tests.
    # The test name for these indicates which index we are intentionally 'missing' for.
    # A few of these tests are effectively repeats of a few we've already done, but it is better to be clear about
    # the coverage and how the tests are composed and annotated here. Note that the sequence template for many of
    # the early tests does not change (only its used portion does). But full sequencee tests in these sections use
    # a changing sequence as the gap in values (so to speak) moves along for each subsequent test. Because of how
    # processing traverses and can hit edge cases (limits) in many different scenarios (with a variety of exposure
    # to different kinds of bugs, which additionally can only occur in a few unexpected edge cases) this is why we
    # need very thorough coverage in unit tests for this module/algorithm. Also note, that we want to make a thorough
    # comparison of different implementations in this project and even with other libraries.

    def test_algorithm_search_binary__8e_missBeforeList(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (0) @ index None
        ).search(0), None)

    def test_algorithm_search_binary__8e_missForIdx0(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [0, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (1) @ index None
        ).search(1), None)

    def test_algorithm_search_binary__8e_missForIdx1(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [0, 1, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (2) @ index None
        ).search(2), None)

    def test_algorithm_search_binary__8e_missForIdx2(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [0, 1, 2, 4, 5, 6, 7, 8, ]  # 8 elements, term (3) @ index None
        ).search(3), None)

    def test_algorithm_search_binary__8e_missForIdx3(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [0, 1, 2, 3, 5, 6, 7, 8, ]  # 8 elements, term (4) @ index None
        ).search(4), None)

    def test_algorithm_search_binary__8e_missForIdx4(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [0, 1, 2, 3, 4, 6, 7, 8, ]  # 8 elements, term (5) @ index None
        ).search(5), None)

    @function_headline
    def test_algorithm_search_binary__8e_missForIdx5(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [0, 1, 2, 3, 4, 5, 7, 8, ]  # 8 elements, term (6) @ index None
        ).search(6), None)

    @function_headline
    def test_algorithm_search_binary__8e_missForIdx6(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [0, 1, 2, 3, 4, 5, 6, 8, ]  # 8 elements, term (7) @ index None
        ).search(7), None)

    @function_headline
    def test_algorithm_search_binary__8e_missForIdx7(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [0, 1, 2, 3, 4, 5, 6, 7, ]  # 8 elements, term (8) @ index None
        ).search(8), None)

    @function_headline
    def test_algorithm_search_binary__8e_missAfterList(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   # Indices
            [1, 2, 3, 4, 5, 6, 7, 8, ]  # 8 elements, term (9) @ index None
        ).search(9), None)



    # Higher Element Tests

    @function_headline
    def test_algorithm_search_binary__18e_t21_i11(self):
        self.assertEqual(bsearch(
            #0  1  2  3  4  5  6  7   8   9  10  11  12  13  14  15  16  17     # Indices
            [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 15, 21, 22, 23, 25, 28, 29, 30, ]  # 18 elements, term (21) @ index 11
        ).search(21), 11)
        #


if __name__ == '__main__':
    unittest.main(verbosity=2)


##
#

