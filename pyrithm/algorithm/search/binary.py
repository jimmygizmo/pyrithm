
V_: bool = True

# TODO: Subclass ?
class BinarySearchIterative:
    """Binary search algorithm, iterative implementation, full-featured but simple. No special optimizations."""

    def __init__(self, sorted_int_list: list[int]):
        self.s_list: list[int] = sorted_int_list
        if len(self.s_list) == 0:
            raise ValueError("You must initialize with a sorted integer list of at least one integer.")

    def search(self, term: int) -> int|None:
        if V_:
            print(f"BinarySearchIterative running...    Search term: {term}\n"
                     f"List element count (length): {len(self.s_list)}")
            print(f"[{', '.join(str(x) for x in self.s_list)}, ]")

        # TODO: Move these vars to instance vars?
        attempt: int = 0
        traversal: list[str] = []
        min_index: int = 0
        max_index: int = len(self.s_list) - 1
        mid_index: int = (len(self.s_list) // 2)
        if mid_index < min_index:
            mid_index = min_index  # In this case, always 0
        selected_side_length: int = len(self.s_list)
        selected_side: str|None = 'START'
        while True:
            attempt += 1
            traversal.append(selected_side[0])  # because string[0] is the first character of the string (also a list)
            if V_: print(f"ATTEMPT: ({attempt})    current side: {selected_side}    traversal: {''.join(traversal)}\n"
                         f"  min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}\n"
                         f"  selected_side_length: {selected_side_length}")

            if self.s_list[mid_index] == term:
                if V_: print(f"[* FOUND *] term ({term}) at index: {mid_index}    Steps/attempts: {attempt}")
                return mid_index

            if min_index == max_index:
                if V_: print(f"[~ term NOT found ~] ({term})  Exit rule:  min_index == max_index")
                return None

            if self.s_list[mid_index] < term:
                right_length: int = max_index - mid_index  # --RIGHT-- side selected for next search step.
                if V_: print(f"    The term ({term}) > the mid_index element value ({self.s_list[mid_index]}).\n"
                             f"    Next search: RIGHT side. right_length: {right_length}")
                new_right_min_index: int = mid_index + 1
                if new_right_min_index > max_index:  # min can't move right past max for new right side
                    new_right_min_index = max_index
                new_right_mid_index: int = (mid_index + 1) + (right_length // 2)  # This plus 1 moves us past the now-checked mid_index.
                if new_right_mid_index > max_index:  # mid can't move right past max for new right side
                    new_right_mid_index = max_index
                min_index = new_right_min_index
                mid_index = new_right_mid_index
                selected_side = 'RIGHT'
                selected_side_length = right_length
            else:
                left_length: int = mid_index - min_index  # --LEFT-- side selected for next search step.
                if V_: print(f"    The term ({term}) < the mid_index element value ({self.s_list[mid_index]}).\n"
                             f"    Next search: LEFT side. left_length: {left_length}")
                new_left_max_index: int = mid_index - 1
                if new_left_max_index < min_index:  # max can't move left past min for new left side
                    new_left_max_index = min_index
                new_left_mid_index: int = min_index + (left_length // 2)
                if new_left_mid_index < min_index:  # mid can't move left past min for new left side
                    new_left_mid_index = min_index
                max_index = new_left_max_index
                mid_index = new_left_mid_index
                selected_side = 'LEFT'
                selected_side_length = left_length

