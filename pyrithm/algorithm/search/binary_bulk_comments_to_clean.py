
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

# UPDATE - NEW PLAN: Initially I was considering the mid_index element to be part of the LEFT side in some of my
# calculations, but this looks like one of my main problems. IN FACT, after we check the mid_index element for == term,
# we need never check it again. Thus, it needed not be part of ANY side and should not be. It is aparent now to me
# that this is logically critical and I should build my side-choice-adjustment calculations based on this now-
# clarified premise. I have been surprised by the struggles I encountered with binary search. If you you get off on the
# wrong foot with your model of the problem or general concepts, you can find yourself with some edge-case problems.
# I'm only having edge-casees fail, but you can't have any cases fail. This is not that complex of a problem but one
# just needs to model it correctly and view each step in a logical manner (close up) and go step by step through runs
# with different data .. ESPECIALLY with your data that fails tests. You need to break down EXACTLY what is happening
# and some cases this leads to the discover that you have started out with a bad mistake in your model or logic.
# This is a great way to learn though. By hitting walls in some areas, you learn the tough areas of specific algorithms
# or data structures and you develop an intuition about where the tough edge-cases live when you are dealing with
# certain kinds of symmetries and certain kinds of processing.
# Where the edge-cases get interesting is where you have a change in symmetries between data and your processing,
# such as the behavior of odd vs even input or the behavior at limits when there is no longer symnmetry on the sides
# of things etc. Think about symmetry and symmetry changes when thinking about edge cases. And note there are differet
# variations on symmetry. You might say that an odd number of things is not symmetrical, BUT if you pick the middle
# element, then you have symmetry on either side of it for lists with big middles, BUT if that is a list with an
# even number of things, you cannot pick any element with symmetry on both sides. There are many many ways of looking
# at symmetry and when it changes along with other conditions. I'm just saying those are also interesting places to try
# to predict edge cases that will need a little bit of extra code to be handled without a problem. Hey, in cases like
# this you need a ROBUST set of unit tests. I have realized that for binary-search and btree and similar processing/
# structures, you need a LOT of unit tests because there are a lot of little edge cases. The data has a big effect on
# how the graph-traversal occurs and what edge-limits you encounter during the variations in traversal and data
# conditions, so you need a lot of UNIT tests to expose all the different code pathways and test them all. Don't leave
# any code pathway untested. Even more importantly, THOROUGHLY test problems like this, becuase you might be missing
# a little code and not realize it. So when I started working on binary search, I did not learn any other solutions
# and I have not looked at any during this process. I wanted to  fall into the pits on my own and get bitten by the
# tougher parts of this problem. Now I think by treating the mid_index element as SEPARATE from the left or right side
# we will divide into if we keep looking, that will result in better logic. I will be adding a lot more unit tests as
# well.

V_: bool = False  # Verbose logging flag. Nothing printed when false. Set true for testing/troubleshooting.
# TODO: Make this configurable so it can be turned on by the caller, particularly for unit tests.


class BinarySearchIterative:
    """Binary search algorithm, iterative implementation, full-featured but simple. No special optimizations."""

    def __init__(self, sorted_int_list: list[int]):
        self.s_list: list[int] = sorted_int_list
        self.traversal: list[str] = []  # A record of the LEFT-vs-RIGHT traversal decisions for a search. This varies with input.
        if len(self.s_list) == 0:
            raise ValueError("You must initialize with a sorted integer list of at least one integer.")

    def search(self, term: int) -> int|None:
        if V_: print(f"\nBinarySearchIterative running...    Search term: {term}\n"
                     f"List element count (length): {len(self.s_list)}")
        attempt: int = 0
        min_index: int = 0
        max_index: int = len(self.s_list) - 1
        mid_index: int = (len(self.s_list) // 2)
        while True:
            attempt += 1
            if V_: print(f"ATTEMPT ({attempt}): "
                         f"min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}")

            # These two checks may end the iterations with either success and the index or failure to locate.
            if self.s_list[mid_index] == term:
                if V_: print(f"FOUND the search term ({term}) at index: {mid_index}    Steps/attempts: {attempt}")
                return mid_index

            # TODO: Analyzing edge case PROBLEM when term = 0 (< first element) Our test data has 1 as minimum at pos 0.
            #          so the element cant be in this list. Should return None but it did not. This was old prob. Prior to refactor.

            if min_index == max_index:
                if V_: print(f"EXIT SEARCH: min_index == max_index")
                return None
            if mid_index > max_index:
                if V_: print(f"EXIT SEARCH: mid_index > max_index")
                return None
            if mid_index < min_index:
                if V_: print(f"EXIT SEARCH: mid_index < min_index")
                return None


            # This check selects which side, left or right, the term belongs in and makes the adjustments to values to
            # search only in the chosen 'side' during the next step and 'discard' the other 'side' of the list.
            # We don't actually change the original sorted list in any way. We only adjust the three pointers to
            # indices in this list which we use to manage all processing.

            if self.s_list[mid_index] < term:
                # Choose --RIGHT-- side, discard left side, set up for search of right side on next iteration.
                # Right side will not include the mid_index element as we have now checked that element explicitly.
                # In fact, because we use floor division, I think that means the mid_index element would NEVER
                # be considered for the right side, separate from the fact that we choose not to include the mid_index
                # element on ANY side. Our model/design is to exclude the mid_index element from ANY side membership
                # For one thing, this elminates a wasted check on an element we already checked; slightly more efficient on average.
                # Most importantly, though, is that to exclude the mid_index element like this most-closely follows the model/concept/design.
                # This will likely lead to the simplest edge-case code additions. This is all part of our refactor thinking.
                right_length: int = max_index - mid_index
                if V_: print(f"The term ({term}) > the mid_index element value ({self.s_list[mid_index]})."
                             f"Next step will search RIGHT side. right_length: {right_length}")
                # TODO: Check for an edge case regarding mid_index + 1 when near the end or starting list is small.
                min_index = mid_index + 1  # We exclude the old mid_index element from the new RIGHT (or ANY) side.
                mid_index = (mid_index + 1) + (right_length // 2)  # Locate new 'floor-half' mid_index, based on starting ONE element AFTER the old mid_index
                # max_index remains unchanged when we choose the right side.
                if V_: print(f"ADJUSTED: min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}")

                # if mid_index == max_index:
                #     if V_:
                #         print(f"EXIT SEARCH via CHOOSE-RIGHT CHECK: mid_index == max_index")
                #     # This means we think we need to look in the RIGHT side, but it is now size zero. Search exhausted.
                #     looking = False  # Can drop this line. The loop will stop when we return.
                #     return None

                # TODO: (THINKKING NO ON THIS NOW) -> Fix might be to make these two end checks do GREATER OR LESS AS WELL AS EQUAL:  CHECK <= and =>
                # OR .. MAYBE NO CHECKS CAN HAPPEN HERE --IF-- WE HAVE AT LEAST A NEW mid_index ELEMENT TO CHECK NEXT LOOP.

            else:
                # Choose --LEFT-- side, discard right side, set up for search of left side on next iteration.
                # Left side will not include the mid_index element as we have now checked that element explicitly.
                left_length: int = mid_index - min_index
                if V_: print(f"The term ({term}) < the mid_index element value ({self.s_list[mid_index]})."
                             f"Next step will search LEFT side. left_length: {left_length}")
                max_index = mid_index - 1  # We exclude the old mid_index element from the new LEFT (or ANY) side.
                # min_index remains unchanged when we choose the left side.
                mid_index = min_index + (left_length // 2)
                # TODO: Explain the above better. NOTE: This is where mid_index can become less than min_index. This might matter for some possible exit logic.
                if V_: print(f"ADJUSTED: min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}")

                # if mid_index == min_index:
                #     if V_:
                #         print(f"EXIT SEARCH via CHOOSE-LEFT CHECK: mid_index == min_index")
                #     # This means we think we need to look in the LEFT side, but it is now size zero. Search exhausted.
                #     looking = False  # Can drop this line. The loop will stop when we return.
                #     return None


# TODO: We could make a parent class to cover a little bit of common code but it does not seem critical that we do so.
class BinarySearchRecursive:
    """Simple recursive implementation of the classic binary search algorithm."""

    def __init__(self, sorted_int_list: list[int]):
        self.sorted_int_list: list[int] = sorted_int_list
        self.traversal: list[str] = []  # A record of the LEFT-vs-RIGHT traversal decisions for a search. This varies with input.
        if len(self.sorted_int_list) == 0:
            raise ValueError("You must initialize with a sorted integer list of at least one integer.")

    def search(self, term: int) -> int|None:
        pass


##
#

