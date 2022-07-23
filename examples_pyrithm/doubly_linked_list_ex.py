#! /usr/bin/env python

import pyrithm

dll = pyrithm.structure.linked_list.DoublyLinkedList()

# ######## About import strategies/styles

# In this example file for a doubly-linked list, I import in a different manner than in the similar example file for
# a singly-linked list. In this case here, I simply import the entire pyrithm package and because of how I designed
# the __init__.py files in the package, this import will also import all of the sub-modules. Resources are not
# of concern in this case, so I don't have any strong reason to only import sub-modules. So now when I initialize,
# I will need to specify the full path into the class I want to use. See related comments in:
# singly_linked_list_ex.py in which I do this alternative import: import pyrithm.structure.linked_list as ll
#
# This is medium-sized topic, which advanced developers should learn well and you can start here:
# For more info see the docs on packages: https://docs.python.org/3/tutorial/modules.html#packages
# This is a sub-topic of the docs on modules: https://docs.python.org/3/tutorial/modules.html#modules
#

# #######  Set up test data

# Some data to work with. Arbitrary objects. Tuples in this case.
# Tuples consisting of a character and an integer. These make it easy to see
# ordering.
objects = [
    ('aa', 11),
    ('bb', 22),
    ('cc', 33),
    ('dd', 44),
    ('ee', 55),
    ('ff', 66),
    ('gg', 77),
    ('hh', 88)
]

print()
print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

print('Example Usage and Basic Tests of pyrithm.structure.linked_list.DoublyLinkedList')
print()
print("""
Each node of the linked list can hold a payload object of any type and to
illustrate this, tuples are used. First we instantiate a linked-list by
calling the constructor:
""")
print()
print(r'dll = pyrithm.structure.linked_list.DoublyLinkedList()')
print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('TEST 1')
print("""
Testing a total of 8 insert_last() operations to build a linked-list. To view
the results, the export() method will be called after each insert to show the
correct functioning. The final export() output should be this list of 8 tuples
in the original order, as indicated by their data:
""")
print(r"[('aa', 11), ('bb', 22), ('cc', 33), ('dd', 44), ('ee', 55), ", end="")
print(r"('ff', 66), ('gg', 77), ('hh', 88)]")
print()
print('TEST 1 RESULTS')
print()

# Create the linked list in the same order as objects using insert_last()
for obj in objects:
    dll.insert_last(obj)
    print(dll.export())

print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('TEST 2')

print("""
The delete() method will be tested next by deleting four nodes which are the
1st, 3rd, 5th and 8th (last) nodes. Deletion is performed by locating nodes
with matching payload data using the Python '==' operator, NOT by position.
The resulting linked-list will be exported for confirmation of success
and it should be:
""")
print(r"[('bb', 22), ('dd', 44), ('ff', 66), ('gg', 77)]")

print("""
The calls to be made are:

dll.delete(('aa', 11))
dll.delete(('cc', 33))
dll.delete(('ee', 55))
dll.delete(('hh', 88))
""")

print('TEST 2 RESULTS:')

dll.delete(('aa', 11))
dll.delete(('cc', 33))
dll.delete(('ee', 55))
dll.delete(('hh', 88))
print()

print(dll.export())

print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('TEST 3')

print("""
The nodes which were deleted will now be put back in place using the four
methods, insert_first(), insert_last(), insert_after() and insert_before().
The resulting linked-list should be the original list, who\'s export should
be:
""")
print(r"[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ", end="")
print(r"('f', 6), ('g', 7), ('h', 8)]")

print()
print('Each call and the resulting export are shown separately for clarity:')
print()

print(r"sll.insert_first(('a', 1))")
obj = ('a', 1)
sll.insert_first(obj)
print(sll.export())
print()

print(r"sll.insert_last(('h', 8))")
obj = ('h', 8)
sll.insert_last(obj)
print(sll.export())
print()

print(r"sll.insert_before(('f', 6), ('e', 5))")
locator_obj = ('f', 6)
obj = ('e', 5)
sll.insert_before(locator_obj, obj)
print(sll.export())
print()

print(r"sll.insert_after(('b', 2), ('c', 3))")
locator_obj = ('b', 2)
obj = ('c', 3)
sll.insert_after(locator_obj, obj)
print(sll.export())
print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

print("""
This has been a basic illustration and test of the pyrithm SinglyLinkedList class.
There are many other tests which can be performed to stress edge cases and
various operations in different contexts. Since object equivalence and
non-equivalence is fundamental to the operation of this class and since there
are many considerations to be made in this area with respect to different
types of objects which could be used as payload objects, much more testing can
and should be done for real-world usage. Please see pyrithm/tests for more
thorough testing of this class through formal unit testing and other types of
testing.

Please also see the related example script: doubly_linked_list_ex.py
The linked_list module also contains the DoublyLinkedList class with similar examples.
A double-linked list takes up more memory but can be faster for certain operations and
there are other differences in its features and of course many aspects of the
implementation are different. It is an excellent learning exercise to carefully
study and compare both.
""")

