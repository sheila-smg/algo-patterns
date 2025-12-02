"""
Given a sorted array of integers nums (which may include negative numbers),
return a new array containing the squares of each number, sorted in non decreasing order.

Your solution must run in O(n) time and use the two pointers technique.
"""

def sorted_squares(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    position = len(nums) - 1
    while left <= right:
        left_square = nums[left]**2
        right_square = nums[right]**2
        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        position -= 1
    return result

def sorted_squares_II(nums):
    left = 0
    right = len(nums) - 1
    result = []
    while left <= right:
        left_square = nums[left]**2
        right_square = nums[right]**2
        if left_square > right_square:
            result.append(left_square)
            left += 1
        else:
            result.append(right_square)
            right -= 1
    return result[::-1]

if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 4, 10]))
    print(sorted_squares_II([-4, -1, 0, 3, 4, 10]))