"""
Last Occurrence of Target

Given a sorted array that may contain duplicates, return the index
of the last occurrence of the target. If the target does not appear,
return -1.

This version of binary search continues searching in the right half
after finding the target, ensuring the rightmost index is returned.
"""

def last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

if __name__ == "__main__":
    print(last_occurrence([1, 2, 2, 2, 3, 4, 5], 2))
    print(last_occurrence([1, 2, 2, 3], 2))