"""
First Duplicate

Given an array of integers `nums`, return the **first number that appears twice**
when scanning the array from left to right.

If no duplicate exists, return None.

Examples:
- nums = [2, 1, 3, 5, 3, 2] -> 3
  (3 is the first value that appears for the second time)

- nums = [1, 2, 3, 4] -> None

Goal:
Use a hash set to track which values have already been seen.
As soon as a value is found in the set, return it immediately.

This pattern is fundamental when detecting repeated elements or cycles
and runs in O(n) time and O(n) space.

Time complexity: O(n)
Space complexity: O(n)
"""

def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

if __name__ == "__main__":
    print(first_duplicate([2, 1, 3, 5, 3, 2]))  # Output: 3
    print(first_duplicate([1, 2, 3, 4]))        # Output: None