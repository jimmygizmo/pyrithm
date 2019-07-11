#! /usr/bin/env python3

import unittest
# https://docs.python.org/3/library/unittest.html

from employee import Employee  # Class to be tested


class TestEmployee(unittest.TestCase):

    @classmethod
    # NOTE: The unittest package uses some camel-case names.
    # This is not best-practice and you should avoid it in your own code.
    def setUpClass(cls):
        print('setUpClass\n')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass\n')

    def setUp(self):
        """Create employee instances used by all tests"""
        print('setUp')  # These prints are for illustrative purposes.
        self.emp_1 = Employee('Jimmy', 'Gizmo', 80000)
        self.emp_2 = Employee('Karen', 'Smith', 90000)

    def tearDown(self):
        print('tearDown\n')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Jimmy.Gizmo@email.com')
        self.assertEqual(self.emp_2.email, 'Karen.Smith@email.com')

        self.emp_1.first = 'Larry'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'Larry.Gizmo@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Jimmy Gizmo')
        self.assertEqual(self.emp_2.fullname, 'Karen Smith')

        self.emp_1.first = 'Larry'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'Larry Gizmo')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.salary, 84000)
        self.assertEqual(self.emp_2.salary, 94500)


if __name__ == "__main__":
    unittest.main()

