"""
Two Sum

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`.

Assumptions:
- Exactly one valid solution exists.
- You cannot use the same element twice.
- Indices should be returned as a list [i, j].

"""

def two_sums(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []

if __name__ == "__main__":
    print(two_sums([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(two_sums([3, 2, 4], 6))      # Output: [1, 2]
    print(two_sums([3, 3], 6))         # Output: [0, 1]
    print(two_sums([1, 2, 3, 4, 5], 8)) # Output: [2, 4]
    print(two_sums([-1, -2, -3, -4, -5], -8)) # Output: [2, 4]