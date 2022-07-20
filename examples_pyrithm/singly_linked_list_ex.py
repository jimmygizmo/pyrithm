#! /usr/bin/env python
# TODO: Reword things and rename some variables to make it clear this example goes with SinglyLinkedList.
# TODO: Make another class for DoublyLinkedList and also make it's accompanying example usage script.
import pyrithm.structure.linked_list as linked_list
# Alternatively: from pyrithm.structure.linked_list import *
# Then we would: sll = SinglyLinkedList()
# TODO: Consider a single module linked_list and then with that we could define the different
# types/classes, including distinguishing the Node class types so they can live side by side,
# such as: SinglyLinkedNode vs. DoublyLinkedNode.
# This might be a good way to organize modules/classes in a medium to large application. Coming up with a good
# class hierarchy is an art and it can change over time as makes sense. Try to get it right the first time since
# changing the class structure later on, probably means needing to update client code simultaneously, so it
# is worthy of some early planning.

sll = linked_list.SinglyLinkedList()

# Some data to work with. Arbitrary objects. Tuples in this case.
# Tuples consisting of a character and an integer. These make it easy to see
# ordering.
objects = [
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4),
    ('e', 5),
    ('f', 6),
    ('g', 7),
    ('h', 8)
]

print()
print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

print('Example Usage and Basic Tests of pyrithm.structure.linked_list')
print()
print("""
Each node of the linked list can hold a payload object of any type and to
illustrate this, tuples are used. First we instantiate a linked-list by
calling the constructor:
""")
print()
print(r'll = pyrithm.structure.linked_list.SinglyLinkedList()')
print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('TEST 1')
print("""
Testing a total of 8 insert_last() operations to build a linked-list. To view
the results, the export() method will be called after each insert to show the
correct functioning. The final export() output should be this list of 8 tuples
in the correct order, as indicated by their data:
""")
print(r"[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ", end="")
print(r"('f', 6), ('g', 7), ('h', 8)]")
print()
print('TEST 1 RESULTS')
print()

# Create the linked list in the same order as objects using insert_last()
for obj in objects:
    sll.insert_last(obj)
    print(sll.export())

print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('TEST 2')

print("""
The delete() method will be tested next by deleting four nodes which are the
1st, 3rd, 5th and 8th (last) nodes. Deletion is performed by locating nodes
with matching payload data using the Python 'is' operator. The resulting
linked-list will be exported for confirmation of success and it should be:
""")
print(r"[('b', 2), ('d', 4), ('f', 6), ('g', 7)]")

print("""
The calls to be made are:

sll.delete(('a', 1))
sll.delete(('c', 3))
sll.delete(('e', 5))
sll.delete(('h', 8))
""")

print('TEST 2 RESULTS:')

sll.delete(('a', 1))
sll.delete(('c', 3))
sll.delete(('e', 5))
sll.delete(('h', 8))
print()

print(sll.export())

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
# TODO: Update wording to match introduction of another class and ex script for DoublyLinkedList
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
""")

