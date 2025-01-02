
import bisect  # Bisect is part of Python's Standard Library, which we use here for comparison to our Pyrithm modules.
# NOTE: We provide a wrapper class, StandardLibraryBisectWrapper for compatibility with our unit tests for this module.


V_: bool = True  # Verbose flag

# New Super Class/Base Class. There is a little bit of code from our 4 implementation classes which we de-duplicate
# here as a best practice. This is one type of refactoring.
class BinarySearch:
    """Base class for binary search algorithm implementations which holds common attributes and code to support
    the 4 different implementations of binary search we have in this module. Validates initialization data."""

    def __init__(self, sorted_int_list: list[int]):
        self.s_list: list[int] = sorted_int_list
        if len(self.s_list) == 0:
            raise ValueError("You must initialize with a sorted integer list (ascending) of at least one integer. "
                             "The supplied list is empty.")
        if not self.verify_sorted():
            raise ValueError("You must initialize with a sorted integer list (ascending). "
                             "The supplied list is not sorted properly.")
        print(f"DEV EXPERIMENT: Base class reports current class as: {__class__.__name__}")

    def verify_sorted(self) -> bool:
        if V_: "Verifying that the list provided for initialization is sorted properly. (Has no out-of-order elements.)"
        result = True
        for i, x in enumerate(self.s_list, start=0):
            # if V_: print(f"{i}: {x}")
            if i > 0:
                if self.s_list[i-1] > self.s_list[i]:
                    result = False
        return result

    def verbose_summarize(self, child_class: str, term: int) -> None:
        print(f"{child_class} running...    Search term: {term}\n"
                 f"List element count (length): {len(self.s_list)}")
        print(f"[{', '.join(str(x) for x in self.s_list)}, ]")


class BinarySearchIterative(BinarySearch):
    """Binary search algorithm, iterative implementation, full-featured but simple. No special optimizations."""
    def __init__(self, sorted_int_list: list[int]):
        super().__init__(sorted_int_list)

    def search(self, term: int) -> int|None:
        if V_: self.verbose_summarize(__class__.__name__, term)

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


class StandardLibraryBisectWrapper(BinarySearch):
    """TODO: Write this docstring"""
    def __init__(self, sorted_int_list: list[int]):
        self.s_list: list[int] = sorted_int_list
        super().__init__(sorted_int_list)

    def search(self, term: int) -> int|None:
        if V_: self.verbose_summarize(__class__.__name__, term)
        return self.bisect_left_wrapper(term)

    def bisect_left_wrapper(self, term: int) -> int|None:
        i = bisect.bisect_left(self.s_list, term)
        if i != len(self.s_list) and self.s_list[i] == term:
            if V_:
                print(f"StdLib's bisect.bisect_left: [* FOUND *] term at index: {i}\n")
            return i
        else:
            if V_:
                print(f"StdLib's bisect.bisect_left: [~ term NOT found ~]\n")
            return None





