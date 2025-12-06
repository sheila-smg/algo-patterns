"""
Recursive Binary Search

Given a sorted array and a target value, return the index of the target.
If the target is not present, return -1.

This function implements binary search using recursion. Each recursive
call reduces the search space by half. The base case occurs when the
search boundaries cross.
"""

def recursive_binary_search(arr, target, left = None, right = None):
    if left is None:
        left = 0

    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  # Base case: target not found

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)
    
if __name__ == "__main__":
    print(recursive_binary_search([1, 2, 3, 4, 5, 6], 4))