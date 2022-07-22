#! /usr/bin/env python
# TODO: Make another class for DoublyLinkedList and also make it's accompanying example usage script.

import pyrithm.structure.linked_list as ll

sll = ll.SinglyLinkedList()

# ######## About import strategies/styles
#
# I chose my import and alias style for the following reasons. The short 'll' alias is unique and compact
# and there are many cases where you need to shorten longer paths to keep code readable and PEP8 compliant, plus I
# wanted to illustrate this to you. 'll' is not the most readable variable name I will admit, but in this example
# I like it. In other apps I might use something longer. It would be totally fine to just use the same name for the
# alias as the lowest level module you are importing, such as: 'import pyrithm.structure.linked_list as linked_list'
#
# Obviously, this style of importing allows me to make a shorter call when I initialize the SinglyLinkedList class.
# Also, Pyrithm is sort of a toolkit style of library in which there are many very related parts, but many of those
# are standalone and so it is likely that the user will be reaching down into the namespace in which the individual
# 'tools' (or classes etc) are located, rather than referencing higher level objects as with other kinds of libraries
# that do things like provide a complex service, in which case many classes/modules are not so standalone.
# Pyrithm is the type of library in which the organization of modules and directories for the user's sake,
# even for executables such as this example script, so longer names are likely unless aliases are used.
# Personally I might prefer to just 'import pyrithm', but I wanted to give an illustration of these other concepts
# which perhaps apply more often in
# real world applications.
#
# In the current program, there would be no problem with 'import pyrithm' because this does not require many
# resources and this would result in nice and explicit usage, like this:
# sll = pyrithm.structure.linked_list.SinglyLinkedList()
# If you wanted to limit what you import a bit more, perhaps to conserve resources then that is another reason you
# might use one of many styles of importing sub-modules and probably also assigning them aliases in many cases.
# This is medium-sized topic, which advanced developers should learn well and you can start here:
# For more info see the docs on packages: https://docs.python.org/3/tutorial/modules.html#packages
# This is a sub-topic of the docs on modules: https://docs.python.org/3/tutorial/modules.html#modules
#
# Note that in the similar example for Doubly Linked List, I do a different import style, to illustrate the options.
#


# #######  Set up test data

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
print(r'sll = pyrithm.structure.linked_list.SinglyLinkedList()')
print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('TEST 1')
print("""
Testing a total of 8 insert_last() operations to build a linked-list. To view
the results, the export() method will be called after each insert to show the
correct functioning. The final export() output should be this list of 8 tuples
in the original order, as indicated by their data:
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
with matching payload data using the Python '==' operator, NOT by position.
The resulting linked-list will be exported for confirmation of success
and it should be:
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

