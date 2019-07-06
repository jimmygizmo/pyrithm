#! /usr/bin/env python3

# Examples of list comprehensions in various formats

# List comprehension with nested fors
list_a = [x*y for x in range(10) for y in range(x, x+10)]

# Might as well print it with a list comprehension too, just for fun.
[print(a) for a in list_a]  

