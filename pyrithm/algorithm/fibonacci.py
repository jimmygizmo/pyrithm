
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

#TODO: Update the init.sh file for reformatting, better info and autopep8 install


# TODO: Replace the contents of the class with recursive_fibonacci.
# This cache speeds things up in a MASSIVE way.
# Able to go to n=1100 and probably way beyond even though the python/system stack limit is 1000
# import sys
# print(sys.getrecursionlimit())
# Still running super fast at n=1100 and number of digits is probably 400-500 at that point.
# TODO: Fix the highest_n_cached cache optimizer. has a little error currently.
#
fibo_cache = {}
highest_n_cached = 0

def recursive_fibonacci(n):
    #if n < highest_n_cached:  # Optimization but not yet defined error. huh?
    if n in fibo_cache:
        return fibo_cache[n]
    if n<=1:
        fibo_cache[n] = n
        #highest_n_cached = n
        return n
    else:
        value = recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
        fibo_cache[n] = value
        #highest_n_cached = value
        return value


# TODO: Would be very interesting to do multiple speed comparisions:
# 1. Iteration method below once it is fixed.
# 2. recursive_fibonacci(n) raw, no optimizations.
# 3. recursive_fibonacci(n) with just caching using the if in keys search.
# 4. recursive_fibonacci(n) with the caching and the highest_n_cached optimization
# Number just does an integer comparision rather than having to many or all dict keys.
# Even though scanning the keys appears to go very quickly at least up to near the recursion
# depth limit, noting that we might be able to go way past this recursion limit because of some
# Python or OS feature.


class Fibonacci():

    def __init__(self):
        pass
    
    # TODO: FIX. Back to basics for the fix. At any position/member 'n', to calculate the member's
    # value, we must know the two preceeding members. At n=0, there are zero preceeding members.
    # At n=1, there is only one preceeding member, so for both n=0 and n=1 we a have a special
    # edge case.
    # That's TWO positions of members we have the edge case for AND it is TWO members we need to
    # satisfy the calculation input requirements for .. so ..
    # have the 2 preceeding values
    def by_iteration_alpha(self, target_n: int) -> int:
        """Return the nth element of the Fibonacci sequence by iteratively calculating it."""
        # We call the argument target_n so we can refer to n in comments without confusion.
        # The n=0 element is a special edge case when calculating iteratively in this manner.
        if target_n == 0:
            return 0
        # The n=1 element is also a special edge case because we need at least 2 members present
        # in the sequence, in order for the loop to operate below as currently designed.
        # This is only the first implementation method, hence it is marked _alpha. We will
        # explore other implementation methods in this class and the preferred method will
        # be aliased to the symbol 'member' so we can always call the preferred implementation
        # via member(n). The alias is made at the end of the different implementation method
        # definitions.
        if target_n == 1:
            return 1
        # HACK:
        #iteration = 0
        # The following is a hack in the sense that I observed output and realized that the
        # sequence was missing the n=1 member, but had the n=0 member correct (form the edge
        # case code) and had all sequence members correct from n=2 and onwards. So by deduction
        # concluded I needed to include an addition edge case for n=1 and also by deduction I
        # realized I needed to shift the iteration counter back one to make things work.
        # I do not want to leave things like this. I want to have a clearly understood design,
        # not one made to work be a hack deduced from output, even if the design ends up
        # identical, I want to fully understand my original mistake and make all the comments
        # and variable names as correct as possible according to a well thought out design.
        # The hack/fix will be applied on the next commit so this can be easily seen in code diffs.
        iteration = 1
        previous_member = 0  # Initialization value, not really a previous member
        # To use the loop below we also need to handle an edge case of sorts and initlize
        # the current_current member which is the n=1 member as we begin the iterations.
        # And the n=1 member of course has a value of 1.
        current_member = 1
        while not iteration == target_n+1:
            sum = current_member + previous_member
            previous_member = current_member
            current_member = sum
            iteration += 1
        
        return current_member


    # Alias the symbol 'member' to the preferred function used to calculate the nth member.
    # In this way we can have multiple calculation methods, but also use the most logical
    # name as an alias to the currently preferred method available in this class.
    member = by_iteration_alpha  # Preferred method of calculating the nth member; member(n).

##
#

class fib_member():
    def __init__(self, fib_member: two_previous, fib_member: one_previous, value: int):
        self.two_previous = two_previous
        self.one_previous = one_previous
        self.value = value
    
    sef advance_one(self):



