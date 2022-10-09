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
print()
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
print()
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

print("""
Doubly-linked lists have almost twice the complexity within their implementation
as a singly linked list and there are more special edge-cases. The export() method
we have been using is not enough to show that our links to parent and child are
correct across operations. So we have the dump() method. This will show the full
detail of the IDs of the nodes and the references to nodes in the parent and child
attributes or None if that is the case. This allows full validation/debugging.
The following is the dump of our doubly-linked list after these 4 delete operations:
""")

print()
print()
dll.dump()
print()


print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print()
print('TEST 3')

print("""
The nodes which were deleted will now be put back in place using the four
methods, insert_first(), insert_last(), insert_after() and insert_before().
The resulting linked-list should be the original list, who\'s export should
be:
""")
print(r"[('aa', 11), ('bb', 22), ('cc', 33), ('dd', 44), ('ee', 55), ", end="")
print(r"('ff', 66), ('gg', 77), ('hh', 88)]")

print()
print('Each call and the resulting export are shown separately for clarity:')
print()

print(r"dll.insert_first(('aa', 11))")
obj = ('aa', 11)
dll.insert_first(obj)
print(dll.export())
print()

print(r"dll.insert_last(('hh', 88))")
obj = ('hh', 88)
dll.insert_last(obj)
print(dll.export())
print()

print(r"dll.insert_before(('ff', 66), ('ee', 55))")
locator_obj = ('ff', 66)
obj = ('ee', 55)
dll.insert_before(locator_obj, obj)
print(dll.export())
print()

print(r"dll.insert_after(('bb', 22), ('cc', 33))")
locator_obj = ('bb', 22)
obj = ('cc', 33)
dll.insert_after(locator_obj, obj)
print(dll.export())
print()


print('- - - - - - - -')
print()
print("""
Let's do one more insert_before and target the first node so we test this special case.
We will use a unique payload. This is one of those important edge cases to test.
Notice how the type structure of the payload actually changed. '00' is a string now
whereas all the other items in this position were integers. This is totally allowed.
The type of object contained in each node can be anything at all. Just remember that
since we completely compare all aspects of the objects that are involved in using
this class as payloads or locators/query-items and initializers .. the caveats of
object equivalence apply and this technique can be SLOW, relatively speaking,
but very flexible. Also, there are many ways to speed things up for specific use-cases
of a doubly-linked list.
""")

print(r"dll.insert_before(('aa', 11), ('##', 00))")
locator_obj = ('aa', 11)
obj = ('##', '00')
dll.insert_before(locator_obj, obj)

print()
print(r"An export of the resulting final linked list. Please verify correctness:")
print(dll.export())
print()


print('- - - - - - - -')
print()
print("""
Also, let's do one more insert_after and target the last node so we test this special case.
We will use a unique payload. This is one of those important edge cases to test.
""")

print(r"dll.insert_after(('hh', 88), ('**', 99))")
locator_obj = ('hh', 88)
obj = ('**', 99)
dll.insert_after(locator_obj, obj)

print()
print(r"An export of the resulting final linked list. Please verify correctness:")
print(dll.export())
print()


print('- - - - - - - -')
print()
print("""
Again, we dump the full detail of the doubly-linked list, showing memory addresses
of the objects and especially the parent and child links. Please manualy verify that
all links are correct. The formatting of this output makes it pretty easy.
""")

print()
dll.dump()
print()


print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print()
print('TEST 4')

print("""
DoublyLinkedList has a private _find() method which is not actually used internally
but is there for illustration. It finds through == object comparison/equivalence which
is a non-trivial topic one should study. This test starts at a specified node and in
our test we specify the head and then the find traverses the list downwards and
compares each payload object in detail until it finds the 'equivalent' payload
(again .. equivalence caveats apply with this technique) and if and when
a node payload matches the locator object, the found node's memory address
is printed. This address can then be compared to the dump output from TEST 3
to confirm the correct node was located. Please do so.

NOTE: On indicating 'private' with underscore: I realize I am calling a private method
from an external test but Python does not enforce against this. The leading underscore in
the _find() method name does cause a highlighted warning in my IDE to go
along with the convention of such an underscore. I could make a public find method,
which is fine, but I will leave this method private and leave these comments, because
the conventions around private methods and naming in Python are also important to
learn. Most IDEs will highlight and warn about leading underscore private access issues
'import *' wildcard imports and some other factors are actually affected, so in truth,
there ARE functional issues with _private_method_name() leading underscore naming
and it is more than just a convention or tradition. There is no effect on what can be
called or accessed from where, however as Python remains a very permissive,
free-form language, which is why Python is so great!

The call which will be made is this:

dll._find(dll.head, ('dd', 44))

This call looks for the object payload for of this exact tuple ('dd', 44).
Please check the memory address shown here to that from the dump output for
the node for ('dd', 44) in the preceding TEST 3.
""")

locator_obj = ('dd', 44)
# Find can be started at any node, but we just start at the head. We could make _find just start at the head always
# and remove the optional starting point argument. TODO: Consider doing this for both linked list types.
result = dll._find(dll.head, locator_obj)
print(result)

print()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

print("""
DoublyLinkedList TESTS CONCLUSION

This has been a basic illustration and test of the Pyrithm DoublyLinkedList class.
There are many other tests which can be performed to stress edge cases and
various operations in different contexts. Since object equivalence and
non-equivalence is fundamental to the operation of this class and since there
are many considerations to be made in this area with respect to different
types of objects which could be used as payload objects, much more testing can
and should be done for real-world usage. Please see pyrithm/tests for more
thorough testing of this class through formal unit testing and other types of
testing.

Please also see the related example script: singly_linked_list_ex.py
The linked_list module also contains the SinglyLinkedList class with similar examples.
A singly-linked list takes up less memory but can be slower for certain operations and
there are other differences in its features and of course many aspects of the
implementation are different. It is an excellent learning exercise to carefully
study and compare both.
""")

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print()

