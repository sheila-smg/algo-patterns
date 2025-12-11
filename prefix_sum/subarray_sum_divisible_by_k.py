"""
Subarray Sum Divisible by K

Given an array of integers `nums` and an integer `k`, return the number of
non-empty continuous subarrays whose sum is divisible by `k`.

This problem uses a prefix sum combined with a hashmap, but instead of tracking
exact sums, it tracks prefix sums modulo `k`.

Key Insight:
If two prefix sums have the same remainder when divided by `k`, the subarray
between them has a sum divisible by `k`.

Approach:
- Maintain a running prefix sum.
- Compute the remainder of the prefix sum modulo `k`.
- Use a hashmap to count how many times each remainder has appeared.
- For each remainder, add its frequency to the result.
- Initialize the hashmap with {0: 1} to count subarrays starting at index 0.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def subarray_sum_divisible_by_k(nums, k):
    remainder_count = {0: 1}
    current_sum = 0
    total_count = 0
    for num in nums:
        current_sum += num
        remainder = current_sum % k
        if remainder in remainder_count:
            total_count += remainder_count[remainder]
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
    return total_count

if __name__ == "__main__":
    print(subarray_sum_divisible_by_k([4, 5, 0, -2, -3, 1], 5))  # Output: 7
    print(subarray_sum_divisible_by_k([5], 9))  # Output: 0
    print(subarray_sum_divisible_by_k([7, -3, 2, 1, 4], 5))  # Output: 6
    print(subarray_sum_divisible_by_k([1, 2, 3, 4, 5], 3))  # Output: 7
    print(subarray_sum_divisible_by_k([-1, 2, 9], 2))  # Output: 2
    