"""
Upper Bound

Given a sorted array, return the index of the first element that is
strictly greater than the target. If no such element exists, return
the length of the array.

This pattern is the counterpart of lower_bound and is commonly used to
compute ranges, count occurrences, and find insertion positions after
the last occurrence of a value.
"""

def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    result = len(arr)
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

if __name__ == "__main__":
    print(upper_bound([1, 2, 4, 4, 5, 6], 4))  # Output: 4
    print(upper_bound([1, 2, 4, 4, 5, 6], 3))  # Output: 2
    print(upper_bound([1, 2, 4, 4, 5, 6], 6))  # Output: 6
    print(upper_bound([1, 2, 4, 4, 5, 6], 0))  # Output: 0