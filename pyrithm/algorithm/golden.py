

import pyrithm.algorithm.fibonacci as fibonacci


class Golden():

    """

    Calculate the golden ratio to the specified accuracy level using the
    Fibonacci sequence by increasing n for the comparision of the (n)th to
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

