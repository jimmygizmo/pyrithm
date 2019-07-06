#! /usr/bin/env python3

# Examples of list comprehensions in various formats.

# This is the basic format of a list comprehension:

# [ expression for item in list if conditional ]

# This is equivalent to:

# for item in list:
#     if conditional:
#         expression

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Example A

print()
print('Example A via list comprehension:')
# Features nested fors and an operation on the iteration variables.
list_a = [x*y for x in range(5) for y in range(x, x+5)]

# Might as well print it with a list comprehension too, just for fun.
[print(a) for a in list_a]  

print()
print('Example A via traditional code:')
list_aa = []
for x in range(5):
    for y in range (x, x+5):
        list_aa.append(x*y)

for aa in list_aa:
    print(aa)

# The two above techniques are verified to produce identical output.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Example B

print()
print('Example B via list comprehension:')
# This list comprehension features a filtering if clause at the end and a
# function call on the iteration variable.
# Unrelated to list comprehension, it also features enumerate() and the
# usage of list() to convert a string to a list of characters.
# A twist here is that the enumeration index variable i is used to calculate
# even vs. odd elements in order to filter out the odd elements.
list_b = [x.upper() for (i, x) in \
          enumerate(list('abcdefghijklmnopqrstuvwxyz')) if (i % 2 == 0)]

[print(b) for b in list_b]  # Again, print it with a list comprehension.

print()
print('Example B via traditional code:')
list_bb = []
alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
for (i, x) in enumerate(alphabet_list):
    if (i % 2 == 0):  # The letter is in an even-numbered position
        list_bb.append(x.upper())

for bb in list_bb:
    print(bb)

# The two above techniques are verified to produce identical output.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Example C

print()
print('Example C via list comprehension:')
# This list comprehension features a variation on filtering where the
# the expression or opertion on the main iteration which in this case is
# upper() is only performed on the words in even positions, otherwise the
# words in the odd positions are left unchanged via the else clause occuring
# in the expression in the first section of the list comprehension. In a sense,
# this is the conditional application of the expression section, rather than
# simple filtering by use of a conditional at the end of the list
# comprehension in the conditional section.
phrase = 'the quick brown fox jumped over the lazy dog'

list_c = [word.upper() if (i % 2 == 0) else word for (i, word) in \
          enumerate(phrase.split())]

[print(c) for c in list_c]  # Again, print it with a list comprehension.

print()
print('Example C via traditional code:')
list_cc = []
word_list = phrase.split()
for (i, word) in enumerate(word_list):
    if (i % 2 == 0):  # The word is in an even-numbered position
        new_word = word.upper()
    else:
        new_word = word
    list_cc.append(new_word)

for cc in list_cc:
    print(cc)

# The two above techniques are verified to produce identical output.

