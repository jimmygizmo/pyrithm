
import pyrithm.algorithm.fibonacci as fibonacci


class Golden:

    """

    Calculate the golden ratio to the specified accuracy level using the
    Fibonacci sequence by increasing n for the comparison of the (n)th to
    (n-1)th sequence member value ratios until the required number of digits
    reach stability.

    Provide a method to convert the golden ratio to the golden angle.
    Provide methods to invert the golden ratio and golden angle.

    """

    def __init__(self, digits: int):
        """Initialize an instance of the Golden class for an accuracy level
        of the specified number of digits."""
        self.digits: int = digits
    
    # TODO: Complete this module and the user/example code to demonstrate it.
    # I am still debating whether or not to use the typing module and static
    # type checking here, since I generally want to start doing this, but it
    # may not be justifiable for smaller modules such as this.

    # WIll return a string because if we returned floats (which is actually
    # the true data type) then because we might want to see many many decimal
    # places, we my see exponential notation being applied which is not what
    # we want. Maybe there is a way to turn off exponential notation or use
    # a special math/number class so we can still return a float but be able
    # to see up to maybe 60-80 decimal places. One of the goals of pyrithm's
    # fibonacci and golden modules is to see the interesting numbers up to
    # a very high accuracy level and to play around with the desired accuracy
    # level and see how it all works.
    def find_accurate_ratio(self) -> str:
        n = 0
        ratios = []
        # TODO: Finish the main logic in this method. A few helper methods
        # are started below. We might need one or two more helper methods.


    
    def has_enough_digits(self, value: str) -> bool:
        return len(value) >= self.digits

    def identical_digits(self, a: str, b: str) -> int:
        la = len(a)
        lb = len(b)
        identical_digits = 0
        # TODO: Finish this method