#! /usr/bin/env python

import pyrithm.algorithm.fibonacci as fibonacci

fib_gen = fibonacci.fibbonacci_generator()  # The generator function is called.
# fib_gen = fibonacci.fibbonacci_generator_one_based()

print('n  nth Fibonacci sequence member')
print('-  -----------------------------')

# Since the generator method was called, it has now returned an iterator and
# we can call next() on it. Note that a generator, returned by a generator
# function IS also an iterator.
for n in range(0, 40):
    print(f"{n}  {next(fib_gen)}")

