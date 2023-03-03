#! /usr/bin/env python


print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\nIterables and Iterators\n")


# An iterable is a container from which you can get an iterable.
# This is possible because iterables have two special methods on their objects:
# __iter__() returns an iterator.
list_iterable = ["up", "down", "left", "right", ]


print(f"\nType of list_iterable: {type(list_iterable)}")
print(f"Id (address) of list_iterable: {id(list_iterable)}")

print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


my_iterator = list_iterable.__iter__()
print(f"\nType of my_iterator - made using __iter--(): {type(my_iterator)}")
print(f"Id (address) of my_iterator: {id(my_iterator)}")

print("\nYou can see the object types shown and that the Ids show that each is a different object.")
print("\nNow lets iterate by calling next() on the iterator object:")

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print("\n\nAnd now lets iterate by calling the __next__() method of a fresh iterator object.")
print("\nThe first iterator object my_iterator has exhausted all of its iterations so we make my_iterator2:")

my_iterator2 = list_iterable.__iter__()

print(my_iterator2.__next__())
print(my_iterator2.__next__())
print(my_iterator2.__next__())
print(my_iterator2.__next__())

print("\nThese are uquivalent.")

print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

my_iterator3 = iter(list_iterable)  # same thing
print(f"\nType of my_iterator3 - made using iter(): {type(my_iterator3)}")
print(f"Id (address) of my_iterator3: {id(my_iterator3)}")

# The for operator actually creates an iterator from an iterable and then calls the next() method on each item.
# Or you can pass it an object that is already an iterator.

print("\nPrinting from a for loop of an iterable (a list):")
for item in list_iterable:
    print(item)


print("\nPrinting from a for loop of an iterator made from that same list:")
for item in my_iterator3:
    print(item)


print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


print("\nWe can make an iterator from a string which is also an iterable and iterate over each character.\n")

a_string_is_also_an_iterable = "abcdefg"
string_iterator = iter(a_string_is_also_an_iterable)


for item in string_iterator:
    print(item)

