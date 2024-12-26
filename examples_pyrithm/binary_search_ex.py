#! /usr/bin/env python

import pyrithm

# Index:          0  1  2  3  4  5  6  7   8   9  10  11  12  13  14  15  16  17
my_sorted_list = [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 15, 21, 22, 23, 25, 28, 29, 30, ]  # 18 elements

bsearch_iter = pyrithm.algorithm.search.binary.BinarySearchIterative(my_sorted_list)
bsearch_recur = pyrithm.algorithm.search.binary.BinarySearchRecursive(my_sorted_list)

print(f"Sorted list to search:\n{', '.join(map(str, my_sorted_list))}")

search_term_1 = 21  # This is at index 11.
search_term = search_term_1

print(f"I want the zero-based index; the position of: {search_term}")
print(f"The value [None] will be returned if the term is not present in the list.")



found_index = bsearch_iter.search(search_term)
if found_index:
    print(f"Found the index: {found_index}")
else:
    print(f"The search term was not located in the supplied list.")




