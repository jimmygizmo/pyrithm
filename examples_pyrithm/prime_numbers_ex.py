#! /usr/bin/env python

import pyrithm.algorithm.prime as prime

print('n  All prime numbers between zero and 200, inclusive.')
print('-  --------------------------------------------------')

for n in range(0, 200 + 1):
    # primality = 'PRIME' if prime.Prime.is_prime(n) else '-----'
    print(f"{n}  { 'PRIME' if prime.Prime.is_prime(n) else '-----' }")

