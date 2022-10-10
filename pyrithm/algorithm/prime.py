

class Prime:
    """
    Provide utility methods to determine of a number is a prime number. Instances of Prime can be created with
    a cache of pre-computed prime numbers over a specified range for a performance enhancement.
    Optional ways to use these features are provided.
    The first 10 prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
    """
    VERBOSE = False
    DEBUG = False

    # Optional cache of pre-calculated results such as what pyrithm.algorithm.fibonacci has.
    # There are many use-cases where caching a pre-computed value is helpful, even for relatively simple calculations.
    #_cache = []  # These class variables will no longer be used. Changing to per-instance caches.
    #_cache_max_pre_compute = 0  # This is not the max prime value in the cache. This is the largest pre_compute value.

    @staticmethod
    def is_divisible_by(dividend, divisor):
        return dividend % divisor == 0

    @staticmethod
    def is_prime(x: int) -> bool:
        if x < 2:  # Edge case because 1 is not a prime number but would pass our algorithmic checks below.
            return False
        # The second argument to range() is not included in the range and this works well, because we already
        # know that x is divisible by x exactly one time, and so we do not need to check it.
        for divisor in range(2, x):  # I believe we can stop checking earlier, but exactly where? x/2? (x/2)+1?
            if Prime.is_divisible_by(x, divisor):
                if Prime.DEBUG:
                    print(f"{divisor} is a factor of {x} so {x} cannot be a prime number. "
                          f"No additional factors need to be tried.")
                return False
        return True

    def __init__(self, pre_compute: int):
        """
        Initialize an instance of Prime. If a pre_compute integer value is given, look for all prime numbers
        that may exist between 0 and pre_compute and save all of those prime numbers in the instance's cache.
        Values up to and including the pre_cache value itself will be included when they are a prime number.
        # TODO: Verify the 'up to and including' aspect.
        """
        self.cache = []
        self.cache_max_pre_compute = pre_compute  # Doesn't seem like we need this now with instance-level cache.

        if pre_compute < 2:
            raise ValueError("The pre_compute constructor argument of Prime() must be an integer > 1.")

        if Prime.VERBOSE:
            print(f"Pre-populating class-level prime number cache for pre_compute value: {pre_compute}")

        for n in range(1, pre_compute + 1):
            if Prime.is_prime(n):
                if Prime.VERBOSE:
                    print(f"{n} is a prime number. Adding it to the cache.")
                self.cache.append(n)
        else:
            if Prime.VERBOSE:
                print(f"No additional pre-computing needed. _cache_max_pre_compute: {self.cache_max_pre_compute}")

