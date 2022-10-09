#! /usr/bin/env python

import pyrithm.algorithm.prime as prime

VERBOSE = True

print("\n")
print(f"This example creates an instance of the Prime class, in contrast to the static example.")
print(f"When instantiating an instance, we can specify a maximum value up to which to pre-compute prime number"
      f"values.")
print("\n")

prime_class_instance = prime.Prime(100)
print("\n")

prime_class_instance_smaller_pcomp = prime.Prime(40)
print("\n")

prime_class_instance_larger_pcomp = prime.Prime(200)
print("\n")

# Try an invalid pre_compute value. It should throw an exception as a ValueError.
prime_class_instance_invalid_pcomp = prime.Prime(1)
print("\n")

# print(prime_class_instance._cache_max_pre_compute)
#
# print(f"n  All prime numbers between zero and 200, inclusive.")
# print(f"-  --------------------------------------------------")
#
# maximum = 200
# for n in range(1, maximum + 1):  # Plus 1 so we include the maximum value itself.
#     if VERBOSE:
#         print(f"{n}  { 'PRIME' if prime.Prime.is_prime(n) else '- - -' }")
#     else:
#         if prime.Prime.is_prime(n):  # This is a static use. A class static method is called directly.
#             print(n, end="")
#         if n < maximum:
#             print(", ", end="")
# print()
#
# # For the non-verbose output, we want comma-separated values on a single line with no extra comma on the end.
# # We could easily get something like this by pre-calculating everything into an array and then just printing the array.
# # However, we don't want to require pre-calculation and thus waiting in this case (regardless of how fast or slow)
# # so the way we did it, we will output as the numbers are calculated, but will still have the proper formatting
# # for the last item. There are almost always edge-cases to handle in every requirement.
#
