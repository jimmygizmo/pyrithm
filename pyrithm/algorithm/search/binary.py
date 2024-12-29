
V_: bool = True


class BinarySearchIterative:
    """Binary search algorithm, iterative implementation, full-featured but simple. No special optimizations."""

    def __init__(self, sorted_int_list: list[int]):
        self.s_list: list[int] = sorted_int_list
        self.traversal: list[str] = []
        if len(self.s_list) == 0:
            raise ValueError("You must initialize with a sorted integer list of at least one integer.")

    def search(self, term: int) -> int|None:
        if V_: print(f"\nBinarySearchIterative running...    Search term: {term}\n"
                     f"List element count (length): {len(self.s_list)}")
        attempt: int = 0
        min_index: int = 0
        max_index: int = len(self.s_list) - 1
        mid_index: int = (len(self.s_list) // 2)
        # TODO: Possibly:
        # left_length: int = mid_index - min_index
        # right_length: int = max_index - mid_index
        # TODO: IMPORTANT! - If we can do these JUST inside the loop, we need not do them below at all ??!???!!?
        # TODO: This looks doable and would be on a great path to cleaner, simpler code. (Our edge case prob still exists FYI
        #            but it is nicer to solve it with already-simplified code. Might as well do more of this great refactoring
        #            we are getting done before working hard on our 1 little remaining edge case. 46 diverse unit tests now pass. It's just the one..
        while True:
            attempt += 1
            if V_: print(f"ATTEMPT ({attempt}):  "
                         f"min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}")

            if self.s_list[mid_index] == term:
                if V_: print(f"--FOUND-- the search term ({term}) at index: {mid_index}    Steps/attempts: {attempt}")
                return mid_index

            if min_index == max_index:
                if V_: print(f"--failed-- to find term.  Exit rule:  min_index == max_index")
                return None
            if mid_index > max_index:
                if V_: print(f"--failed-- to find term.  Exit rule:  mid_index > max_index")
                return None
            if mid_index < min_index:
                if V_: print(f"--failed-- to find term.  Exit rule:  mid_index < min_index")
                return None

            if self.s_list[mid_index] < term:
                right_length: int = max_index - mid_index  # --RIGHT-- side selected for next search step.
                if V_: print(f"   The term ({term}) > the mid_index element value ({self.s_list[mid_index]}).  "
                             f"Next search: RIGHT side. right_length: {right_length}")
                min_index = mid_index + 1
                mid_index = (mid_index + 1) + (right_length // 2)
                # TODO: Possibly add a (RIGHT) stop here for mid_index
                if V_: print(f"   ADJUSTED:  min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}")
                # TODO: Possibly maintain left_length and right_length in vars so we can use them for our exit checks.
            else:
                left_length: int = mid_index - min_index  # --LEFT-- side selected for next search step.
                if V_: print(f"   The term ({term}) < the mid_index element value ({self.s_list[mid_index]}).  "
                             f"Next search: LEFT side. left_length: {left_length}")
                max_index = mid_index - 1
                mid_index = min_index + (left_length // 2)
                # TODO: Possibly add a (LEFT) stop here for mid_index
                if V_: print(f"   ADJUSTED:  min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}")
                # TODO: Possibly maintain left_length and right_length in vars so we can use them for our exit checks.

