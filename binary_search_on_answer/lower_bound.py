"""
Lower Bound

Given a sorted array, return the index of the first element that is
greater than or equal to the target. If all elements are smaller than
the target, return the length of the array.

This pattern is a classic "binary search on answer" technique, used to
find insertion positions or the earliest feasible value in scheduling
and optimization problems.

"""

def lower_bound(arr, target):
    left = 0
    right = len(arr) - 1
    result = len(arr)
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

if __name__ == "__main__":
    print(lower_bound([1, 2, 4, 4, 5, 6], 4))  # Output: 2
    print(lower_bound([1, 2, 4, 4, 5, 6], 3))  # Output: 2
    print(lower_bound([1, 2, 4, 4, 5, 6], 7))  # Output: 6
    print(lower_bound([1, 2, 4, 4, 5, 6], 0))  # Output: 0