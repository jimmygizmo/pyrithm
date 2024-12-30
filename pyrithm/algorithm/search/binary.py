
V_: bool = True

# TODO: Subclass ?
class BinarySearchIterative:
    """Binary search algorithm, iterative implementation, full-featured but simple. No special optimizations."""

    def __init__(self, sorted_int_list: list[int]):
        self.s_list: list[int] = sorted_int_list
        self.traversal: list[str] = []
        if len(self.s_list) == 0:
            raise ValueError("You must initialize with a sorted integer list of at least one integer.")

    def search(self, term: int) -> int|None:
        if V_: print(f"BinarySearchIterative running...    Search term: {term}\n"
                     f"List element count (length): {len(self.s_list)}")
        # TODO: Move these vars to instance vars?
        attempt: int = 0
        min_index: int = 0
        max_index: int = len(self.s_list) - 1
        # BIG SURPRISE!!! Things seem to be working but I see mid_index-related calcs are off. Attempting fix below here.
        # mid_index: int = (len(self.s_list) // 2) - 1
        mid_index: int = (len(self.s_list) // 2)  # GREAT ! This was a fix. Did not change that all tests are/were passing. BUT, finding suff in fewer attempts! Great.
        # TODO: Trial fix for the latest edge case. Seems like we need this because without it we can successfully
        #         exit with a found status for a nonexistent -1 index. This 1 element list [1] with search(1) triggers the final edge case.
        if mid_index < min_index:
            mid_index = min_index  # In this case, always 0
        # TODO: UPDATE - That fixed it. NO MORE BUGS LEFT!
        #
        # Just need to initialize the lengths here and prior to first loop we don't really have a left/right, so we
        # will initialize to the full size for both, as any logic we do only cares about when lengths approach zero.
        # This is more correct especially for really small lists like one or two element lists. Our other option is to
        # use None, but we need to watch out for creating an unnecessary need for limit checks when right here all we
        # want to do is initialize these without creating some edge case that is a false exit condition for small lists.
        left_length: int = max_index - min_index
        right_length: int = max_index - min_index
        selected_side: str|None = 'START'
        while True:
            attempt += 1
            if V_: print(f"ATTEMPT ({attempt}):  "
                         f"min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}\n"
                         f"side: {selected_side}    left_length: {left_length}    right_length: {right_length}")

            if self.s_list[mid_index] == term:
                if V_: print(f"[* FOUND *] term ({term}) at index: {mid_index}    Steps/attempts: {attempt}")
                return mid_index

            if min_index == max_index:
                if V_: print(f"[~ term NOT found ~] ({term})  Exit rule:  min_index == max_index")
                return None
            if mid_index > max_index:
                if V_: print(f"[~ term NOT found ~] ({term})  Exit rule:  mid_index > max_index")
                return None
            if mid_index < min_index:
                if V_: print(f"[~ term NOT found ~] ({term})  Exit rule:  mid_index < min_index")
                return None

            if self.s_list[mid_index] < term:
                right_length = max_index - mid_index  # --RIGHT-- side selected for next search step.
                if V_: print(f"   The term ({term}) > the mid_index element value ({self.s_list[mid_index]}).  "
                             f"Next search: RIGHT side. right_length: {right_length}")
                new_right_min_index: int = mid_index + 1
                if new_right_min_index > max_index:  # min can't move right past max for new right side
                    new_right_min_index = max_index
                new_right_mid_index: int = (mid_index + 1) + (right_length // 2)  # This plus 1 moves us past the now-checked mid_index.
                if new_right_mid_index > max_index:  # mid can't move right past max for new right side
                    new_right_mid_index = max_index
                min_index = new_right_min_index
                mid_index = new_right_mid_index
                selected_side = 'RIGHT'
            else:
                left_length = mid_index - min_index  # --LEFT-- side selected for next search step.
                if V_: print(f"   The term ({term}) < the mid_index element value ({self.s_list[mid_index]}).  "
                             f"Next search: LEFT side. left_length: {left_length}")
                new_left_max_index: int = mid_index - 1
                if new_left_max_index < min_index:  # max can't move left past min for new left side
                    new_left_max_index = min_index
                new_left_mid_index: int = min_index + (left_length // 2)
                if new_left_mid_index < min_index:  # mid can't move left past min for new left side
                    new_left_mid_index = min_index
                max_index = new_left_max_index
                mid_index = new_left_mid_index
                selected_side = 'LEFT'

