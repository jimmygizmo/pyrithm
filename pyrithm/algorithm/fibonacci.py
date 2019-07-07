

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


class FibbonacciIteratorZeroBase():

    """

    Implement the Fibonacci sequence using an iterator.

    """

    # This is an attempt to make the iterator solution begin the sequence at
    # 0 just like the recursive solution does. See relevant comments above.

    # TODO: How about implementing caching (a massive performance benefit to
    # the recursive implementation) to this iterator implementation .. or is
    # it even necessary?
    # NOTE: The iterator solutions seem to run very fast and my not need
    # caching, but we need to test more at higher n values and analyze the
    # design a bit more to be sure.

    def __init__(self):
        # self.prev_prev is actually non-existent at the point of
        # initialization since this would equate to member for n = -1 which
        # is not part of the definition of the Fibbonacci sequence, but we
        # have chosen a style of the sequence which starts at n=0 where this
        # 'first' memeber is 0 and to make this iterator implementation work
        # correctly, this is how we have to initialize it. The implementation
        # details are not important. What is important is that we have
        # consistent behavior and everything works, regardless of the
        # implementation details.
        self.prev_prev = 0
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        # We must save the previous value before we shift everything because we
        # want a Fibbonacci sequence that starts at 0, not at 1. An iterator
        # solution is a lot simpler if we just let it start at 1 but we want
        # a sequence identical to the recursive implementation and have already
        # made this style choice, which in my opinion more closely matches the
        # definition and starting at zero inherenently 'feels' more correct.
        return_val = self.prev  # Essential for a sequence that starts at 0.
        self.prev_prev = self.prev
        self.prev = self.curr
        self.curr = self.prev + self.prev_prev
        return return_val  # We had to save it to be able to return it here.

