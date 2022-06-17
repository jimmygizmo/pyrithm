#! /usr/bin/env python

import pyrithm.algorithm.fibonacci as fibonacci

#fib_iter = fibonacci.FibbonacciIterator()
fib_iter = fibonacci.FibbonacciIteratorZeroBasedSimple()

print('n  nth Fibonacci sequence member')
print('-  -----------------------------')


for n in range(0, 40):
    print(f"{n}  {next(fib_iter)}")

