from typing import List

"""
Implementation of Selection Sort

- Best Complexity: O(n^2)
- Worst Complexity: O(n^2)
- Average Complexity: O(n^2)
"""


def selection_sort(array: List[int], size: int) -> List[int]:
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[min_idx] > array[i]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])

    return array
