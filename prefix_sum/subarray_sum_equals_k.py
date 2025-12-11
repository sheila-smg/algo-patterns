"""
Subarray Sum Equals K

Given an array of integers `nums` and an integer `k`, return the total number
of continuous subarrays whose sum equals `k`.

The array may contain negative numbers, which means a sliding window approach
does not apply. This solution uses a prefix sum combined with a hashmap to
track previously seen cumulative sums.

Approach:
- Maintain a running prefix sum.
- For each position, check how many times (current_sum - k) has appeared so far.
- Use a hashmap to store frequencies of prefix sums.
- Initialize the hashmap with {0: 1} to handle subarrays starting at index 0.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def subarray_sum_equals_k(nums, k):
    prefix_sum_count = {0: 1}
    current_sum = 0
    total_count = 0
    for num in nums:
        current_sum += num
        complement = current_sum - k
        if complement in prefix_sum_count:
            total_count += prefix_sum_count[complement]
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
    return total_count


if __name__ == "__main__":
    print(subarray_sum_equals_k([1, 1, 1], 2))  # Output: 2
    print(subarray_sum_equals_k([1, 2, 3], 3))  # Output: 2
    print(subarray_sum_equals_k([-1, -1, 1], 0))  # Output: 1
    print(subarray_sum_equals_k([3, 4, 7, 2, -3, 1, 4, 2], 7))  # Output: 4
    print(subarray_sum_equals_k([1, -1, 0], 0))  # Output: 3