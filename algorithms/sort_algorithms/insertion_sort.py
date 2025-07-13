from typing import List

"""
Implementation of Insertion Sort

- Best Complexity: O(n^2)
- Worst Complexity: O(n^2)
- Average Complexity: O(n^2)
"""


def insertion_sort(array: List[int], size: int):
    for step in range(1, size):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array
