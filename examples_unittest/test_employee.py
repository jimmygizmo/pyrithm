#! /usr/bin/env python3

import unittest
# https://docs.python.org/3/library/unittest.html

from employee import Employee  # Class to be tested


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Jimmy', 'Gizmo', 80000)
        emp_2 = Employee('Karen', 'Smith', 90000)

        self.assertEqual(emp_1.email, 'Jimmy.Gizmo@email.com')
        self.assertEqual(emp_2.email, 'Karen.Smith@email.com')

        emp_1.first = 'Larry'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'Larry.Gizmo@email.com')
        self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        emp_1 = Employee('Jimmy', 'Gizmo', 80000)
        emp_2 = Employee('Karen', 'Smith', 90000)

        self.assertEqual(emp_1.fullname, 'Jimmy Gizmo')
        self.assertEqual(emp_2.fullname, 'Karen Smith')

        emp_1.first = 'Larry'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'Larry Gizmo')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        emp_1 = Employee('Jimmy', 'Gizmo', 80000)
        emp_2 = Employee('Karen', 'Smith', 90000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.salary, 84000)
        self.assertEqual(emp_2.salary, 94500)


if __name__ == "__main__":
    unittest.main()

