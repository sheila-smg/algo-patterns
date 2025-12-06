"""
Exercise: First Occurrence (Leftmost Index)

Given a sorted list that may contain duplicate values, write a function that
returns the index of the first occurrence of a given target. If the target
is not present, return -1.

This exercise focuses on:
- Detecting when to continue searching the left half after finding the target
- Maintaining correct boundary updates to ensure the result is the leftmost index
- Handling duplicates without scanning linearly
- Using binary search structure while modifying the mid comparison logic
"""

def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left < len(arr) and arr[left] == target:
        return left
    return -1

def first_occurrence_classic(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left =  mid + 1
        else:
            right = mid - 1
    return result


if __name__ == "__main__":
    print(first_occurrence([1, 2, 2, 2, 3, 4, 5], 2))
    print(first_occurrence_classic([1, 2, 2, 2, 3, 4, 5], 2))
    print(first_occurrence([1, 2, 2, 3], 2))
    print(first_occurrence_classic([1, 2, 2, 3], 2))

