

class Prime:

    VERBOSE = False

    """
    Generate a sequence of prime numbers. Determine if an integer is a prime number.
    A prime number is a whole number greater than 1 whose only factors are 1 and itself.
    The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.


    """

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
                    print(f"{divisor} is a factor of {x} so {x} cannot be a prime number.")
                return False
        return True

    def __init__(self):
        """Initialize an instance of Prime."""
        pass

