from typing import List

"""
Implementation of Bubble Sort

- Best Complexity: O(n)
- Worst Complexity: O(n^2)
- Average Complexity: O(n^2)
"""


def bubble_sort(array, size) -> List[int]:
    for step in range(size - 1):
        for i in range(size - step - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array
