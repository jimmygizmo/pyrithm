

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
        """Return the nth member of the sequence. Use caching. Use cache
        lookup optimization."""

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
            member_value = self.member_slow(n - 1) + self.member_slow(n - 2)
            return member_value


class FibbonacciIterator():

    """

    Implement the Fibonacci sequence using an iterator.

    """

    # NOTE: This implementation differs from the above recursive implementation
    # in that the sequence it can generate begins with the value 1, whereas
    # the above recursive implementation begins with the value 0, followed by
    # 1 etc. Different sources define the Fibbonacci sequence in either way
    # and it seems to be a matter of preference if you define it as:
    # 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
    # or as:
    # 1, 1, 2, 3, 5, 8, 13, 21 ...
    # In this case the iterator implementation simply lends itself to starting
    # at 1 as it is currently written.
    # TODO: Can we make a simple modification of this iterator implementation
    # which will begin at 0 like the above recursive implementation?
    # TODO: How about implementing caching (a massive performance benefit to
    # the recursive implementation) to this iterator implementation .. or is
    # it even necessary?
    # Both of these TODOs would be excellent to explore further.

    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

