

class Prime:
    """
    Generate a sequence of prime numbers. Determine if an integer is a prime number.
    A prime number is a whole number greater than 1 whose only factors are 1 and itself.
    The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
    """
    VERBOSE = True

    # Optional cache of pre-calculated results such as what pyrithm.algorithm.fibonacci has.
    # There are many use-cases where caching a pre-computed value is helpful, even for relatively simple calculations.
    _cache = []
    _cache_max_pre_compute = 0  # This is not the max prime value in the cache. This is the largest pre_compute value.

    @staticmethod
    def is_divisible_by(dividend, divisor):
        return dividend % divisor == 0

    @staticmethod
    def is_prime(x: int) -> bool:
        if x < 2:  # Edge case because 1 is not a prime number but would pass our algorithmic checks below.
            return False
        # We cannot check all the way up to x because x/x we know is 1 and is allowed for prime numbers. Stop at x-1.
        for divisor in range(2, x - 1):  # I believe we can stop checking earlier, but exactly where? x/2? (x/2)+1?
            if Prime.is_divisible_by(x, divisor):
                if Prime.VERBOSE:
                    print(f"{divisor} is a factor of {x} so {x} cannot be a prime number. "
                          f"No additional factors need to be tried.")
                return False
        return True

    def __init__(self, pre_compute: int):
        """
        Initialize an instance of Prime. If a pre_compute integer value is given, look for all prime numbers
        that may exist between 0 and pre_compute and save all of those prime numbers in the Prime class cache.
        This cache is available to all instances. The cache will be as large as the largest pre_compute value
        requested by any instance, thus it can serve all the instances. If the cache is already large enough,
        no additional pre-computing of prime numbers will be performed. Values up to and including the
        pre_cache value itself will be included when they are a prime number. (Of course this is all educational,
        as I don't see a huge need for instances of this class in practice, but it is a good illustrative case.
        Prime number code could work fine as a static class or a static module with no OO at all, but I am
        trying to cover many Python topics with the Pyrithm library and provide a lot of good code and design
        patterns which can be reused.)
        """
        if pre_compute < 2:
            raise ValueError("The pre_compute constructor argument of Prime() must be an integer > 1.")

        if pre_compute > Prime._cache_max_pre_compute:
            if Prime.VERBOSE:
                print(f"Pre-populating class-level prime number cache for pre_compute value: {pre_compute}")
            # TODO: This very dumbly rebuilds the entire cache. Make it start where it left off, if it can.
            Prime._cache = []
            for n in range(1, pre_compute + 1):
                if Prime.is_prime(n):
                    if Prime.VERBOSE:
                        print(f"{n} is a prime number. Adding it to the cache.")
                    Prime._cache.append(n)
        else:
            if Prime.VERBOSE:
                print(f"No additional pre-computing needed. _cache_max_pre_compute: {Prime._cache_max_pre_compute}")

