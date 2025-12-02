"""
Container With Most Water

Given an array of non negative integers 'height' where each element represents
the height of a vertical line drawn at position 'i', find two lines that,
together with the x axis, form a container that holds the maximum amount of water.

The amount of water the container can store is determined by:
    min(height[left], height[right]) multiplied by the horizontal distance (right minus left).

Return the maximum amount of water that can be stored.

Examples:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Input: height = [1,1]
    Output: 1
"""

def container_with_most_water(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

if __name__ == "__main__":
    print(container_with_most_water([1, 8, 6, 5, 2, 3, 9, 2, 5, 7]))






