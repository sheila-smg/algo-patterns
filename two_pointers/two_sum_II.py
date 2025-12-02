"""
Two Sum II

Given a sorted array of integers `numbers` and an integer `target`,
return the indices (1 indexed) of the two numbers such that they add up to `target`.

Assume that exactly one valid solution exists.

Your solution must use the two pointers technique and run in O(n) time.
"""

def two_sum_II(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    print(two_sum_II([2, 7, 11, 15, 19], 17))