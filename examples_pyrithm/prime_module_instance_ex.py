#! /usr/bin/env python

import pyrithm.algorithm.prime as prime

VERBOSE = False

print("\n")
print(f"This example script creates an instance of the Prime class, in contrast to the static example which just "
      f"uses static methods within the class (see prime_numbers_ex.py).")
print(f"Each instance of Prime can have its own cache of pre-computed prime numbers for a performance boost over "
      f"that range. This is a generic concept for you to learn from and adapt to other OOP use-cases.")
print(f"When creating an instance, we can specify the maximum value up to which to pre-compute (search for) "
      f"prime number values.")
print()

print("Created an instance with a small pre_compute of 30.")
prime_class_instance_30 = prime.Prime(30)
print()

print("Created an instance with a medium pre_compute of 100.")
prime_class_instance_100 = prime.Prime(100)
print()

print("Created an instance with a large pre_compute of 1000.")
prime_class_instance_1000 = prime.Prime(1000)
print()

print("Created an instance with an extra-large pre_compute of 40000. Please wait 5-10 seconds for this one ...")
prime_class_instance_20000 = prime.Prime(40000)
print("Whew! That one actually took a noticeable amount of hard work by the CPU for a few seconds there.")
print()


print("Looking closer at the instance with the pre_compute of 1000; Let's directly access this cache object.\n")
print("How many actual prime numbers are in this cache? Lets count the cache entries:")
print(len(prime_class_instance_1000.cache))
print(f"What is the last and therefore highest cache entry (prime number): "
      f"{prime_class_instance_1000.cache[-1]}")
print("\n")


print("Let's just see the entire internal cache in this instance. It is just a list, like an array.\n")
print(prime_class_instance_1000.cache)
print("\n")


print("Now we'll recreate the same example as the static usage in the other script, but call the is_prime() method "
      "through the instance we created.")
print("Also, we will use the instance with a pre_compute of only 30, so we can see both cache hits and cache misses "
      "occurring.\n")
print(f"n  All prime numbers between zero and 200, inclusive.")
print(f"-  --------------------------------------------------")

maximum = 200
for n in range(1, maximum + 1):  # Plus 1 so we include the maximum value itself.
    if VERBOSE:
        print(f"{n}  { 'PRIME' if prime_class_instance_30.is_prime(n) else '- - -' }")
    else:
        if prime_class_instance_30.is_prime(n):  # A static method called through an instance.
            print(n, end="")
            if n < maximum - 1:  # This is just for proper comma formatting as the processing output completes.
                print(", ", end="")
            else:
                print()

print("\n")


# Try an invalid pre_compute value. It should throw an exception as a ValueError.
print("Invalid pre_compute of 1. Intentional ERROR follows:\n")
prime_class_instance__invalid_pre_compute = prime.Prime(1)
print("\n")

