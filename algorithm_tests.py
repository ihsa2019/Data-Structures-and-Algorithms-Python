from validations.validation import validation
from common_utils.constants import ORIGINAL_ARRAY, EXPECTED

from algorithms.sort_algorithms.bubble_sort import bubble_sort
from algorithms.sort_algorithms.selection_sort import selection_sort
from algorithms.sort_algorithms.insertion_sort import insertion_sort

@validation(algo_name="Bubble Sort", expected=EXPECTED)
def bubble_sort_test():
    observed = bubble_sort(ORIGINAL_ARRAY, len(ORIGINAL_ARRAY))
    return observed

@validation(algo_name="Selection Sort", expected=EXPECTED)
def selection_sort_test():
    observed = selection_sort(ORIGINAL_ARRAY, len(ORIGINAL_ARRAY))
    return observed

@validation(algo_name="Insertion Sort", expected=EXPECTED)
def insertion_sort_test():
    observed = insertion_sort(ORIGINAL_ARRAY, len(ORIGINAL_ARRAY))
    return observed

def run_algorithms():
    bubble_sort_test()
    selection_sort_test()
    insertion_sort_test()