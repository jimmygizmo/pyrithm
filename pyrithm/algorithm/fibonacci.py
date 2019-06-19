
####################################################################################################

# In 1202 AD, Leonardi Fibonacci introduced the western world to a amazing sequence of numbers
# which is incredibly basic at one level but which expands into beautiful and powerful phenomena
# which reveal fundamental patterns of the Universe and many fundamental patterns of mathematics
# and geometry.
# The Fibonacci sequence and related mathematics can be the topic entire books and perhaps a
# lifetime of study, but at its most basic level it starts as something very simple, which is
# where this module will begin.

# Starting with 0 and 1, each new number in the sequence is the sum of the two before it.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 

# Starting with 

class Fibonacci():

    def __init__(self):
        pass
    
    def by_iteration_alpha(self, target_n: int) -> int:
        """Return the nth element of the Fibonacci sequence by iteratively calculating it."""
        # We call the argument target_n so we can refer to n in comments without confustion.
        # The zeroeth element is a special edge case when calculating iteratively in this manner.
        if target_n == 0:
            return 0
        iteration = 0
        previous_member = 0
        # To use the loop below we also need to handle an edge case of sorts and initlize
        # the current_current member which is the n=1 member as we begin the iterations.
        # And the n=1 member of course has a value of 1.
        current_member = 1
        while not iteration == target_n:
            iteration += 1  # This is effectively n as we progress from this point on.
            # Often counters used to control a while loop are incremented at the end of the
            # loops operations, but the current design requires we do it mostly becuse of
            # the conditional used to control this loop.
            sum = current_member + previous_member
            previous_member = current_member
            current_member = sum
        
        return current_member


    # Alias the symbol 'member' to the preferred function used to calculate the nth member.
    # In this way we can have multiple calculation methods, but also use the most logical
    # name as an alias to the currently preferred method available in this class.
    member = by_iteration_alpha  # Preferred method of calculating the nth member; member(n).

##
#
