#! /usr/bin/env python

import pyrithm.algorithm.golden as golden

# The pyrithm.fibonacci module is used by the pyrithm golden module to
# calculate values of the nth members of the sequence. The pyrithm golden
# module then determines the ratio of two adajacent member values in order
# to approximate the golden ratio or phi, which of course becomes more
# stable and accurate as n increases. The pyrithm golden module will take
# a specified number of decimal places as an accuracy threshold and then
# by comparing adjacent ratios, will determine when n is high enough to
# acheive the desired accuracy level and then return that value and the
# n member index which acheived the requested level of accuracy.

# Once the golden ratio or phi of a specified accuracy is determined, then
# the pyrithm.golden module can also provide the inverse of that ratio, the
# golden angle and the inverse of the golden angle which of course are
# trivial calculations at that point, but very useful variations of phi for
# performing many interesting and powerful types of calculations.

# An instance pyrithm.algorithm.golden.Golden() is initialized with a
# desired accuracy level by specifying the number of digits which must match
# exactly for four consecutive calculations of the golden ratio for
# increasing values of n. We know that if we have seen 4 identical values in
# a row (up to the specified number of digits) then that ratio will be stable
# for that number of digits, from that point onwards. We do not just compare 2
# or even 3 consecutive ratios because the ratio of adjacent Fibonacci
# member values can fluxuate and be unstable early in the sequence. 4 in a row
# ensures stability and is sure to get us past unstable areas in the
# sequence in cases where the required accuracy level is relatively low.

accurate_digits = 12

gold = golden.Golden(12)  # 12 digits in 4 adjacent ratios must match

(n, ratio) = gold.find_accurate_ratio()

print(f'accurate_digits = {accurate_digits}')
print(f'n = {n}')
print(f'golden ratio = {ratio}')

