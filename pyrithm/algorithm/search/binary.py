
import bisect  # Bisect is part of Python's Standard Library, which we use here for comparison to our Pyrithm modules.
# StandardLibraryBisectWrapper is a wrapper class which enables bisect to work with our unit tests for this module.


V_: bool = True  # Verbose logging


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

    def verify_sorted(self) -> bool:
        if V_: "Verifying that the list provided for initialization is sorted properly. (Has no out-of-order elements.)"
        result = True
        for i, x in enumerate(self.s_list, start=0):
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


class BinarySearchIterativeMinimal:
    """Binary search algorithm, iterative implementation, simplfied code style often used in coding tests.
    This is the identical functionality to the inerative version in this module which uses a mature code style.
    In coding tests, time is often of the essence, so I have stripped out everything but the essentials, including
    type hints which I recommend leaving out of timed coding tests unless requested. This class does not even inherit
    the BinarySearch base class. This is as simple as possible, even using shorter variable names."""
    def __init__(self, sorted_int_list):
        self.s_list = sorted_int_list

    def search(self, term):
        imin = 0
        imax = len(self.s_list) - 1
        imid = (len(self.s_list) // 2)
        if imid < imin:
            imid = imin  # In this case, always 0
        while True:
            if self.s_list[imid] == term:
                return imid
            if imin == imax:
                return None

            if self.s_list[imid] < term:  # --RIGHT-- side selected for next search step
                imin = imid + 1  # new imin is set for next step
                if imin > imax:  # min can't move right past max for new right side
                    imin = imax
                new_imid = (imid + 1) + ((imax - imid) // 2)  # imax - imid is the new right side length
                if new_imid > imax:  # mid can't move right past max for new right side
                    new_imid = imax
                imid = new_imid
            else:  # --LEFT-- side selected for next search step
                imax = imid - 1  # new imax is set for next step
                if imax < imin:  # max can't move left past min for new left side
                    imax = imin
                new_imid = imin + ((imid - imin) // 2)  # imid - imin is new left side length
                if new_imid < imin:  # mid can't move left past min for new left side
                    new_imid = imin
                imid = new_imid  # new imid is set for next step. imin does not change for LEFT selects.


class BinarySearchRecursive(BinarySearch):
    """Binary search algorithm, recursive implementation, full-featured but simple. No special optimizations.
    In the recursive implementation which is not minimal and has logging, rather than pass a lot of arguments to
    the inner recursive function (traverse), we choose to move many local variables to instance variables. This is being
    considered for the other classes in this module, but this recursive class has a stronger reason to do that."""
    def __init__(self, sorted_int_list: list[int]):
        self.term: int|None = None  # TODO: If we move to instance variables for other classes, many can go into the base class.
        self.attempt: int = 0  # Only for verbose logging
        self.traversal: list[str] = []  # Only for verbose logging
        self.selected_side: str = 'START'  # Only for verbose logging
        super().__init__(sorted_int_list)
        self.selected_side_length: int = len(self.s_list)  # Only for verbose logging. (Must be after super init.)

    def search(self, term: int) -> int|None:
        self.term = term
        if V_: self.verbose_summarize(__class__.__name__, term)
        min_index: int = 0
        max_index: int = len(self.s_list) - 1
        mid_index: int = (len(self.s_list) // 2)
        if mid_index < min_index:
            mid_index = min_index  # In this case, always 0
        return self.traverse(min_index, max_index, mid_index)

    def traverse(self, min_index: int, mid_index: int, max_index: int) -> int|None:
        self.attempt += 1
        self.traversal.append(self.selected_side[0])  # because string[0] is the first character of the string (also a list)
        if V_: print(f"ATTEMPT: ({self.attempt})    current side: {self.selected_side}    traversal: {''.join(self.traversal)}\n"
                     f"  min_index: {min_index}    mid_index: {mid_index}    max_index: {max_index}\n"
                     f"  selected_side_length: {self.selected_side_length}")

        if self.s_list[mid_index] == self.term:
            if V_: print(f"[* FOUND *] term ({self.term}) at index: {mid_index}    Steps/attempts: {self.attempt}")
            return mid_index

        if min_index == max_index:
            if V_: print(f"[~ term NOT found ~] ({self.term})  Exit rule:  min_index == max_index")
            return None

        if self.s_list[mid_index] < self.term:
            right_length: int = max_index - mid_index  # --RIGHT-- side selected for next search step.
            if V_: print(f"    The term ({self.term}) > the mid_index element value ({self.s_list[mid_index]}).\n"
                         f"    Next search: RIGHT side. right_length: {right_length}")
            new_max_index: int = max_index  # Does not change when RIGHT selected.
            new_min_index: int = mid_index + 1
            if new_min_index > max_index:  # min can't move right past max for new right side
                new_min_index = max_index
            new_mid_index: int = (mid_index + 1) + (right_length // 2)  # This plus 1 moves us past the now-checked mid_index.
            if new_mid_index > max_index:  # mid can't move right past max for new right side
                new_mid_index = max_index
            self.selected_side = 'RIGHT'
            self.selected_side_length = right_length
        else:
            left_length: int = mid_index - min_index  # --LEFT-- side selected for next search step.
            if V_: print(f"    The term ({self.term}) < the mid_index element value ({self.s_list[mid_index]}).\n"
                         f"    Next search: LEFT side. left_length: {left_length}")
            new_min_index: int = min_index  # Does not change when LEFT selected.
            new_max_index: int = mid_index - 1
            if new_max_index < min_index:  # max can't move left past min for new left side
                new_max_index = min_index
            new_mid_index: int = min_index + (left_length // 2)
            if new_mid_index < min_index:  # mid can't move left past min for new left side
                new_mid_index = min_index
            self.selected_side = 'LEFT'
            self.selected_side_length = left_length

        return self.traverse(new_min_index, new_mid_index, new_max_index)  # RECURSE. Push another call onto call stack.


class BinarySearchRecursiveMinimal():
    """Binary search algorithm, recursive implementation, full-featured but simple. No special optimizations.
    In the recursive implementation which is not minimal and has logging, rather than pass a lot of arguments to
    the inner recursive function (traverse), we choose to move many local variables to instance variables. This is being
    considered for the other classes in this module, but this recursive class has a stronger reason to do that.

    This is the identical functionality to the inerative version in this module which uses a mature code style.
    In coding tests, time is often of the essence, so I have stripped out everything but the essentials, including
    type hints which I recommend leaving out of timed coding tests unless requested. This class does not even inherit
    the BinarySearch base class. This is as simple as possible, even using shorter variable names."""
    def __init__(self, sorted_int_list: list[int]):
        self.s_list: list[int] = sorted_int_list
        self.term: int|None = None

    def search(self, term: int) -> int|None:
        self.term = term
        imin: int = 0
        imax: int = len(self.s_list) - 1
        imid: int = (len(self.s_list) // 2)
        if imid < imin:
            imid = imin  # In this case, always 0
        return self.traverse(imin, imax, imid)

    def traverse(self, imin: int, imid: int, imax: int) -> int|None:
        if self.s_list[imid] == self.term:
            return imid

        if imin == imax:
            return None

        if self.s_list[imid] < self.term:  # --RIGHT-- side selected for next search step.
            new_imax: int = imax  # Does not change when RIGHT selected.
            new_imin: int = imid + 1
            if new_imin > imax:  # min can't move right past max for new right side
                new_imin = imax
            new_imid: int = (imid + 1) + ((imax - imid) // 2)  # imid+1 moves us past now-checked imid. (imax - imid) is the new right side length
            if new_imid > imax:  # mid can't move right past max for new right side
                new_imid = imax
        else:  # --LEFT-- side selected for next search step.
            new_imin: int = imin  # Does not change when LEFT selected.
            new_imax: int = imid - 1
            if new_imax < imin:  # max can't move left past min for new left side
                new_imax = imin
            new_imid: int = imin + ((imid - imin) // 2)  # (imid - imin) is new left side length
            if new_imid < imin:  # mid can't move left past min for new left side
                new_imid = imin

        return self.traverse(new_imin, new_imid, new_imax)  # RECURSE. Push another call onto call stack.


class StandardLibraryBisectWrapper(BinarySearch):
    """This wrapper provides to the Standard Library bisect module, the same interface used by Pyrithm's binary search
    module. This allows the large set of unit tests we have for this module to be run against bisect for a nice
    comparison and to firther validate both the unit tests as well as Pyrithm's binary search."""
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


##
#

