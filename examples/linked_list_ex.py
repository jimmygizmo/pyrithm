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

# Create the linked list in the same order as objects using add_last()
for obj in objects:
    ll.insert_last(obj)

# Export and display:
dump = ll.export()

print(dump)


##
#
