"""
Maximum Length Subarray with Sum = K

Given an array of integers `nums` and an integer `k`, return the length of the
longest continuous subarray whose sum equals exactly `k`.

This problem uses a prefix sum combined with a hashmap, but instead of counting
frequencies, the hashmap stores the first index at which each prefix sum appears.

Key Insight:
If prefix[j] - prefix[i] = k, then the subarray from i + 1 to j has sum k.
To maximize the length of such subarrays, we must use the earliest occurrence
of each prefix sum.

Approach:
- Maintain a running prefix sum while iterating through the array.
- Use a hashmap to store the first index at which each prefix sum appears.
- For each index j:
    - If current_sum == k, consider the subarray from index 0 to j.
    - If (current_sum - k) exists in the hashmap, compute the length
      j - first_index[current_sum - k].
- Update the maximum length accordingly.
- Only store the first occurrence of each prefix sum.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def max_length_subarray_sum_k(nums, k):

    prefix_sum_index = {0: -1}
    current_sum = 0
    max_length = 0
    for index, num in enumerate(nums):
        current_sum += num
        if (current_sum - k) in prefix_sum_index:
            max_length = max(max_length, index - prefix_sum_index[current_sum - k])
        if current_sum not in prefix_sum_index:
            prefix_sum_index[current_sum] = index
    return max_length


if __name__ == "__main__":
    print(max_length_subarray_sum_k([1, -1, 5, -2, 3], 3))  # Output: 4
    print(max_length_subarray_sum_k([-2, -1, 2, 1], 1))    # Output: 2
    print(max_length_subarray_sum_k([1, 2, 3], 6))         # Output: 3
    print(max_length_subarray_sum_k([1, 2, 3], 7))         # Output: 0
    print(max_length_subarray_sum_k([3, 1, -1, 4, -2, 2], 5))  # Output: 5