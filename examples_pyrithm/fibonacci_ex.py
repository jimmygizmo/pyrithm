#! /usr/bin/env python3

import pyrithm

fibonacci = pyrithm.algorithm.fibonacci.Fibonacci()

print()
print('Calculate the Fibonacci sequence using recursion and compare '
      'performance when member values are cached. The pyrythim.Fibonacci '
      'class provides two methods: member() and member_slow(). The member() '
      'method features caching and a cache lookup optmization. The '
      'member_slow() method has no performance optimizations and gets very '
      'slow after about n=30 and gets exponentially slower thereafter. '
      'In member_slow(), the call-stack also increases with increasing n and '
      'will probably crash when n gets close to 1000, assuming you could '
      'wait the extremely long time to calculate to that point, which might '
      'take days of calculation time. However, using the simple caching '
      'implememnted in member(), the caclulation of the value for the '
      'members of the fibonacci sequence go extremely fast up to very high '
      'values of n, which I have tested up to n=10,000 at which point the '
      'number of digits in the value are over 2000! Additionally, because '
      'the preceeding sequence values needed to calculate the next value '
      'in this recursive manner are always available in the cache, the call '
      'stack never needs to go more than about 3-4 levels deep and limits '
      'of how high n can go are unknown and for practical purposes, '
      'incredibly high, yielding massive numbers, all precise fibonacci '
      'members. This is a perfect example of how caching data can yield '
      'very significant performance benefits in many situations.')
print()
print('To run these examples, change the below code and try out different '
      'upper limits for the maximum value of in in the range() and also '
      'compare using the fibonacci.member_slow() method with the vastly '
      'faster fibonacci.member() method which uses caching.')

print('n  nth Fibonacci sequence member')
print('-  -----------------------------')
for n in range(0, 40):
    print(f"{n}  {fibonacci.member_slow(n)}")

