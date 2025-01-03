

class Fibonacci:

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


class FibbonacciIterator:

    """

    Implement the Fibonacci sequence using an iterator. Produce the sequence
    in the style which is based at 0 like the recursive implementation above
    is.

    """

    # This is an attempt to make the iterator solution begin the sequence at
    # 0 just like the recursive solution does.

    # TODO: How about implementing caching (a massive performance benefit to
    # the recursive implementation) to this iterator implementation .. or is
    # it even necessary or possible in a similar way? Maybe not.
    # NOTE: The iterator solutions seem to run very fast and may not need
    # caching, but we need to test more at higher n values and analyze the
    # design a bit more to be sure.

    def __init__(self):
        # self.prev_prev is actually non-existent at the point of
        # initialization since this would equate to member for n = -1 which
        # is not part of the definition of the Fibbonacci sequence, but we
        # have chosen a style of the sequence which starts at n=0 where this
        # 'first' member is 0 and to make this iterator implementation work
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


class FibbonacciIteratorOneBased:

    """

    Implement the Fibonacci sequence using an iterator which provides the
    sequence based at 1 instead of 0 for comparison with the above. This is
    not the style we want, but include it here to show that this is actually
    simpler to implement than the zero-based solution we do want (above) when
    using an iterator.

    """

    # It seems to be a matter of preference if you define the sequence as:
    # 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
    # or as:
    # 1, 1, 2, 3, 5, 8, 13, 21 ...
    # In this case the iterator implementation simply lends itself more simply
    # to starting at 1 as it is currently written gere. Notice the above
    # implementation of choice is a little bit more complex.

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


class FibbonacciIteratorZeroBasedSimple:

    """

    Implement the Fibonacci sequence using an iterator which provides the
    sequence based at 0 and do so in the cleanest and simplest code possible.
    The above FibbonacciIterator() seems a bit more complex than it needs
    to be, so this is an attempt at simplification.

    """

    def __init__(self):
        self.prev = 0
        self.curr = 1
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        # This if-else block handles the edge case to provide the first member
        # of the sequence
        if self.n == 0:  # This will only happen once, for the first member.
            self.n = 1
            return 0
        # else:  # This else block is not even necessary unless we wanted to
        #     # support tracking of n and perhaps return it with the value.
        #     n += 1
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


# Fibbonacci as a generator. Also 0-based:
def fibbonacci_generator():
    prev, curr = 0, 1
    zero_member = True
    while True:
        if zero_member:
            zero_member = False  # So this edge case happens only once.
            yield 0
            continue  # So we don't do the following yield in this edge case.
        yield curr
        prev, curr = curr, prev + curr

# Based at 0 is more correct, but notice how simple the implementation is when you base the sequence at 1.
# I don't personally like the Fibbonacci sequence to be 1-based but it seems you always have to have edge-case code
# in any kind of implementation when you want a 0-based sequence. I just think 0-based is more correct for multiple
# reasons, however, you can see here how if you want a 1-based Fibbonacci sequence, the implementations get
# cleaner/simpler. This is the cleanest implementation I know of, assuming you are ok with 1-based.

# Fibbonacci as a generator. Simpler but less-desirable 1-based style:
def fibbonacci_generator_one_based():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

