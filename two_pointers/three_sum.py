"""
    Find all unique triplets in the array that sum to zero.

    This function returns all distinct triplets [a, b, c] such that:
    a + b + c = 0
    The input array may contain duplicates, but the output must not include
    duplicate triplets.

    The algorithm first sorts the array, then fixes one element at a time and
    uses two pointers to efficiently search for complementary pairs that 
    complete the zero-sum triplet.
"""

def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0:
            if nums[i] == nums[i - 1]:
                continue
        left = i + 1
        right = len(nums) - 1
        while left  < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else: 
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
        
    return result

if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, 3, -2, 1, 4, -2, -3]))
