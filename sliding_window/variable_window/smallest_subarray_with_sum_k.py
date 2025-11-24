"""
Smallest Subarray With Sum >= K (variable window)

Given an array of positive integers nums and an integer k,
return the length of the smallest contiguous subarray whose sum
is greater than or equal to k. If no such subarray exists, return 0.

Pattern: sliding window (variable-size)
"""

def smallest_subarray_with_sum_k(nums, k):
    left = 0
    current_sum = 0
    min_length = len(nums) + 1
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= k:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return min_length if min_length != len(nums) + 1 else 0

if __name__ == "__main__":
    print(smallest_subarray_with_sum_k([2, 3, 1, 2, 4, 3], 8))
    print(smallest_subarray_with_sum_k([1, 5, 2, 3, 1, 5, 6, 6, 1, 2, 10], 20))