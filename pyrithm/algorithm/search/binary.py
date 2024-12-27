
# NOTE: All classes in this module are written to handle integers, but minimal modification would allow handling
# of other types.

# NOTE: It is an increasing tradition in Python (with many benefits) to employ strong or moderate typing in
# many places. I like this. In complex Python apps, you will reduce and simplify bugs and the type hint style is
# really nice in my opinion. I like the explicit expression of types a lot and so nearly all of my code specifies
# types these days. TODO: Move this to some docs on this topic. Bring rest of project up to speed.

# A good analogy to keep in mind is how one quickly scans for a name through a box or stack of index cards by
# essentially splitting the stack 'in half' for each 'step' of the search. It's not so important exactly where you
# split the stack each time as long as it is pretty close to the halfway point in each section at each step. The act
# of splitting the stack is to select a single index card representing the mid-point of the stack. Since any stack
# can contain an even or an odd number of index cards, this is why we call it an 'approximate' mid-point and it does
# not need to be an exact mid-mid point for this algorithm to work well. Being very close to an exact mid-point is
# all that is required, so we will tend to pick the mid-point card but when dealing with an even numbered stack, we
# will just choose the convention to 'round down' and pick the lower card just below the midpint of the two equal
# sub-stacks and we can treat this card as the precise mid-point, just as well as if we had an odd number in the stack
# and it in fact was the precise mid-point. Being close works just as well (and we have no choice since you cannot
# split index cards in half) and on average, it will not matter if we choose the card just on the left vs the one just
# on the right of the point where we split the stack each time. What DOES matter is how we adjust calculations based
# on our convention to always pick the lower one; meaning we will use floor division which rounds DOWN (to the left.)
# This matters in the edge cases, when we are almost done searching and when our supplied sorted list is very small.
# TODO: Complete the analogy explanation here, for checking matching and how the search can end with no find, what the
#          edge cases look like. Good analogies are especially valuable when they explain the edge cases well!

DEMO = True


class BinarySearchIterative():
    """Simple iterative implementation of the classic binary search algorithm."""

    def __init__(self, sorted_int_list: list[int]):
        self.s_list = sorted_int_list
        if len(self.s_list) == 0:
            raise ValueError("You must initialize with a sorted integer list of at least one integer.")

    def search(self, term: int) -> int|None:
        if DEMO:
            print(f"BinarySearchIterative running...")
            print(f"list length: {len(self.s_list)}")
        attempt = 0
        looking = True
        min_index = 0
        max_index = len(self.s_list) - 1
        mid_index = (len(self.s_list) // 2) - 1
        while looking:
            attempt += 1
            if DEMO:
                print(f"attempt: {attempt}")
                print(f"min_index: {min_index}")
                print(f"max_index: {max_index}")
                print(f"mid_index: {mid_index}")

            # These two checks may end the iterations with either success and the index or failure to locate.
            if self.s_list[mid_index] == term:
                looking = False  # Can drop this line. The loop will stop when we return.
                return mid_index
            if min_index == max_index or mid_index > max_index or mid_index < min_index:  # Might not need all these casees but its good coverage for any edge cases.
                looking = False  # Can drop this line. The loop will stop when we return.
                return None

            # This check selects which side, left or right, the term belongs in and makes the adjustments to values to
            # search only in the chosen 'side' during the next step and 'discard' the other 'side' of the list.
            # We don't actually change the original sorted list in any way. We only adjust the three pointers to
            # indices in this list which we use.
            if self.s_list[mid_index] < term:
                # Choose right side, discard left side, set up for search of right side next.
                right_length = max_index - mid_index
                if DEMO:
                    print(f"Choosing RIGHT side for next step. right_length: {right_length}")
                # TODO: Check for an edge case regarding mid_index + 1 when near the end or starting list is small.
                min_index = mid_index + 1  # Move min index to start of right side
                mid_index = mid_index + (right_length // 2)  # Locate new 'floor-half' mid_index
                # max_index remains unchanged when we choose the right side.
                if mid_index == max_index:
                    # This means we think we need to look in the RIGHT side, but it is now size zero. Search exhausted.
                    looking = False  # Can drop this line. The loop will stop when we return.
                    return None

            else:
                # Choose left side, discard right side, set up for search of left side next.
                left_length = mid_index - min_index + 1  # SEEMS LIKE WE NEED THE PLUS ONE. TODO: Explain.
                # TODO: Can we say? "Since we do floor division, left side needs the plus one?"
                if DEMO:
                    print(f"Choosing LEFT side for next step. left_length: {left_length}")
                max_index = mid_index  # Can we optimize here? We actually already checked mid_index itself, but our pattern is to search the whole 'side'. Possibly.
                # min_index remains unchanged when we choose the left side.
                mid_index = (min_index - 1) + (left_length // 2)  # Start at min - 1 to get correct mid_index. (we add a length to an index .. so)
                # TODO: Explain the above better. NOTE: This is where mid_index can become less than min_index. This might matter for some possible exit logic.
                if mid_index == min_index:
                    # This means we think we need to look in the LEFT side, but it is now size zero. Search exhausted.
                    looking = False  # Can drop this line. The loop will stop when we return.
                    return None






class BinarySearchRecursive:
    """Simple recursive implementation of the classic binary search algorithm."""

    def __init__(self, sorted_int_list: list[int]):
        self.sorted_int_list = sorted_int_list
        if len(self.sorted_int_list) == 0:
            raise ValueError("You must initialize with a sorted integer list of at least one integer.")

    def search(self, term: int) -> int|None:
        pass


##
#

