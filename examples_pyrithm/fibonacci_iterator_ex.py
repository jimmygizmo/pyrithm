#! /usr/bin/env python3

import pyrithm

fib_iter = pyrithm.algorithm.fibonacci.FibbonacciIterator()

print('n  nth Fibonacci sequence member')
print('-  -----------------------------')


for n in range(0, 40):
    print(f"{n}  {next(fib_iter)}")

