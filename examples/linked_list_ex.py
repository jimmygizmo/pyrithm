#! /usr/bin/env python3

import pyrithm.structure.linked_list

ll = pyrithm.structure.linked_list.LinkedList()

# Some data to work with. Arbitrary objects. Tuples in this case.
# Tuples consisting of a character and an integer. These make it easy to see ordering.
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
print('Example usage and basic tests of pyrithm.structure.linked_list:')

print()
print('TEST 1')
print()
print('Testing a total of 8 insert_last() operations to create a linked-list. To view the results, '
      'the export() method will be called after each insert to show the correct functioning. '
      'The final export() output should be this list of 8 tuples in the correct order,'
      'as indicated by their data:')
print(r"[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8)]")
print('Running test ...')
print()

# Create the linked list in the same order as objects using insert_last()
for obj in objects:
    ll.insert_last(obj)
    print(ll.export())

print()

print()
print('TEST 2')
print()

print('The delete() method will be tested next by deleting the nodes with the following payload '
      'objects which are the 1st, 5th and 8th (last) nodes. Deletion is performed by locating '
      'nodes with matching payload data using the Python == operator. The resulting linked list '
      'will be exported for confirmation of success and it should be: ')
print(r"[('b', 2), ('c', 3), ('d', 4), ('f', 6), ('g', 7)]")
print('Running test ...')

ll.delete(('a', 1))
ll.delete(('e', 5))
ll.delete(('h', 8))
print()

print(ll.export())

print()


##
#
