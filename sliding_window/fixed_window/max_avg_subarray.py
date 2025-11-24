"""
Maximum Average Subarray (fixed window)
Given an array nums and an integer k, find the maximum average
value across all contiguous subarrays of length k.
Pattern: sliding window (fixed-size)
"""

def max_average_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k


if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(max_average_subarray(nums, k))