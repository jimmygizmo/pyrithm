

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


    @staticmethod
    def _is_divisible_by(dividend, divisor):
        return dividend % divisor == 0


    # TODO: We should add computed values to the cache. We could insert the value into its sequential position, but
    # that would be expensive but would allow determination of the max value etc. Or, we could just append the new
    # values and give up on any order that any pre-computed values might have. The cache membership check will work
    # in either case, but our example that checks that maximum would not work as it currently is. In other words,
    # the maximum prime number in the cache would not no longer also be guaranteed to be the last value in the cache
    # list.


    @staticmethod
    def _is_prime(x: int) -> bool:
        if x < 2:  # Edge case because 1 is not a prime number but would pass our algorithmic checks below.
            return False
        # The second argument to range() is not included in the range and this works well, because we already
        # know that x is divisible by x exactly one time, and so we do not need to check x itself.
        for divisor in range(2, x):  # TODO: I believe we can stop checking earlier, but exactly where? x/2? (x/2)+1?
            if Prime._is_divisible_by(x, divisor):
                if Prime.DEBUG:
                    print(f"{divisor} is a factor of {x} so {x} cannot be a prime number. "
                          f"No additional factors need to be tried.")
                return False
        return True


    def __init__(self, pre_compute: int):
        """
        Initialize an instance of Prime. If a pre_compute integer value is given, look for all prime numbers
        that may exist between 0 and pre_compute and save all of those prime numbers in the instance's cache.
        Values up to and including the pre_compute value itself will be included when they are a prime number.
        """
        self.cache = []
        self.cache_max_pre_compute = pre_compute  # Doesn't seem like we need this now with instance-level cache.

        if pre_compute < 2:
            raise ValueError("The pre_compute constructor argument of Prime() must be an integer > 1.")

        if Prime.VERBOSE:
            print(f"Pre-populating class-level prime number cache for pre_compute value: {pre_compute}")

        for n in range(1, pre_compute + 1):
            if Prime._is_prime(n):
                if Prime.VERBOSE:
                    print(f"{n} is a prime number. Adding it to the cache.")
                self.cache.append(n)


    def is_prime(self, x: int) -> bool:
        # First check this instance's cache to leverage a possible pre-computed entry and return True if the number
        # is found in the cache and if not then perform the calculation and return appropriately.
        if x in self.cache:
            if Prime.DEBUG:
                print(f"cache HIT for: {x}")
            return True
        else:
            if Prime.DEBUG:
                print(f"cache miss for: {x}")
            if Prime._is_prime(x):
                return True
            else:
                return False

