
####################################################################################################
# This module provides generator methods. It is not necessary to provide a class which creates
# instances in this case. Generators themselves sort of create 'instances' of iterators.
# This is more for illustrative/educational purposes rather than real-world applications.


# The generated iterator always has a finite limit.
def flip_flop_generator(max_flip_flops=4):
    """Generates an iterator which returns alternating values of 'flip' or 'flop' up to the maximum of
    max_flip_flops times. If not specified, the max is 4. The first value returned will be 'flip'.
    When the max is exceeded, the standard iterator exception of StopIteration will be raised.
    """
    # Initialize iterator
    state = 'flop'
    count = 0

    # Iteration logic for this generator
    while not (count >= max_flip_flops):
        if state == 'flop':
            state = 'flip'
        else:
            state = 'flop'
        count += 1
        yield state


# The generated iterator is capable of unlimited iterations.
def binary_flip_flop_generator(max_flip_flops=0):
    """Generates an iterator which returns alternating values of 0 or 1 up to the maximum of
    max_flip_flops times, with the ability to iterate an unlimited number of times. If not specified,
    the max is infinite/unlimited iterations, which is specified by setting max_flip_flops to 0. The
    first value returned will be 0. If a non-zero max is specified and is then exceeded, the standard
    iterator exception of StopIteration will be raised.
    """
    # Initialize iterator
    state = 1
    count = 0
    iterate = True

    # Iteration logic for this generator
    while iterate:
        if state == 1:
            state = 0
        else:
            state = 1
        count += 1
        if not (max_flip_flops == 0):
            if (count >= max_flip_flops):
                iterate = False
        yield state


##
#
