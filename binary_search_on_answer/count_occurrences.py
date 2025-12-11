"""
Count Occurrences of Target

Given a **sorted** array that may contain duplicates, return the number
of times the target appears in the array. If the target does not appear,
return 0.

This problem combines binary search variants (first occurrence and
last occurrence) to compute the count efficiently without scanning
the array linearly.

"""

from first_occurrence import first_occurrence_classic
from last_occurrence import last_occurrence

def count_occurrences(arr, target):
    first_index = first_occurrence_classic(arr, target)
    if first_index == -1:
        return 0  # Target not found

    last_index = last_occurrence(arr, target)
    return last_index - first_index + 1

if __name__ == "__main__":
    print(count_occurrences([1, 2, 2, 2, 3, 4, 5], 2))  # Output: 3
    print(count_occurrences([1, 2, 2, 3], 2))          # Output: 2
    print(count_occurrences([1, 2, 3, 4, 5], 6))       # Output: 0
    print(count_occurrences([], 1))                     # Output: 0