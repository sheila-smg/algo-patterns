"""
Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return the length of the
**longest consecutive elements sequence**.

A consecutive sequence is a set of numbers where each value is exactly
1 greater than the previous one, e.g. {4, 5, 6, 7}.

You must write an algorithm that runs in **O(n)** time.

Examples:
- nums = [100, 4, 200, 1, 3, 2]
  The longest consecutive sequence is {1, 2, 3, 4} with length = 4

- nums = [0, 1, 3, 7, 2, 5, 8, 4, 6]
  The array contains a full sequence from 0 to 8, so the answer is 9.

Constraints:
- You may assume nums has length >= 1

Goal:
Use a hash set for O(1) membership checks.
For each number, only start expanding a sequence if it is the *start*
(i.e. num - 1 is not in the set). This ensures O(n) total time.

"""

def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
    print(longest_consecutive([0, 1, 3, 7, 2, 5, 8, 4, 6]))  # Output: 9