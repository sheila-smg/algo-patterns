"""
Exercise: Classic Binary Search

Implement an iterative function that searches for a target value inside a
sorted list and returns its index if present, or -1 otherwise.

The goal is to practice:
- Setting correct left and right boundaries
- Computing the midpoint safely
- Updating the search range based on comparisons
- Stopping the loop at the correct condition (left > right)

This exercise serves as the baseline version from which all other binary
search variants in this folder will build.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    print(binary_search([1, 1, 1], 2))
    print(binary_search([1, 1], 1))
    print(binary_search([], 1))