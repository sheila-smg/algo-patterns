"""
Longest Subarray With Sum <= K (variable window)

Given an array of positive integers nums and an integer k,
return the length of the longest contiguous subarray whose sum
is less than or equal to k.

Pattern: sliding window (variable-size)
"""

def longest_subarray_with_sum_k(nums, k):
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum > k:
            current_sum -= nums[left]
            left += 1
            
        max_length = max(max_length, right - left + 1)
            
    return max_length

if __name__ == "__main__":
    print(longest_subarray_with_sum_k([2, 3, 4, 5, 1, 2, 3, 8, 7, 6, 3, 2, 4], 21))