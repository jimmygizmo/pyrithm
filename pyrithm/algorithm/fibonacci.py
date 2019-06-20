

class Fibonacci():

    """

    Implement the Fibonacci sequence using recursion. The first member of the
    sequence is indexed at n = 0. Cache member values during processing.
    Optimize cache operation by tracking the highest n with a cache entry.

    """

    member_cache = {}
    max_cache_n = 0

    def __init__(self):
        """Initialize an instance of FibonacciRecursive."""
        pass

    def member(self, n):
        """Return the nth member of the sequence. Use caching."""

        if n <= Fibonacci.max_cache_n:
            if n in Fibonacci.member_cache:  # TODO: Always redundant?
                return Fibonacci.member_cache[n]
        if n <= 1:
            Fibonacci.member_cache[n] = n
            Fibonacci.max_cache_n = n
            return n
        else:
            member_value = self.member(n - 1) + self.member(n - 2)
            Fibonacci.member_cache[n] = member_value
            Fibonacci.max_cache_n = n
            return member_value
         
    def member_slow(self, n):
        """Return the nth member of the sequence. Do not use caching."""

        if n <= 1:
            return n
        else:
            member_value = self.member(n - 1) + self.member(n - 2)
            return member_value

