#! /usr/bin/env python

import pyrithm.algorithm.prime as prime

VERBOSE = True

print(f"n  All prime numbers between zero and 200, inclusive.")
print(f"-  --------------------------------------------------")

maximum = 200
for n in range(1, maximum + 1):  # Plus 1 so we include the maximum value itself.
    if VERBOSE:
        print(f"{n}  { 'PRIME' if prime.Prime._is_prime(n) else '- - -' }")
    else:
        # Normally we don't call _protected members directly, but this is an educational demo code and the fact is,
        # Python does not stop you from such access, but your IDE will likely give a warning here, but Python won't.
        if prime.Prime._is_prime(n):  # This is a static use. A class static, protected method is called directly.
            print(n, end="")
            if n < maximum - 1:  # This is just for proper comma formatting as the processing output completes.
                print(", ", end="")
            else:
                print()
print()

# For the non-verbose output, we want comma-separated values on a single line with no extra comma on the end.
# We could easily get something like this by pre-calculating everything into an array and then just printing the array.
# However, we don't want to require pre-calculation and thus waiting in this case (regardless of how fast or slow)
# so the way we did it, we will output as the numbers are calculated, but will still have the proper formatting
# for the last item. There are almost always edge-cases to handle in every requirement.

