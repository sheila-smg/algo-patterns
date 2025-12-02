"""
Trapping Rain Water

Given an array of integers `height` representing an elevation map
where the width of each bar is 1, compute how much water it can trap
after raining.

Examples:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: 6 units of water are trapped between the bars.

    Input: height = [4,2,0,3,2,5]
    Output: 9

"""


def trapping_rain_water(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]
    return water_trapped

if __name__ == "__main__":
    print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 4, 2, 1, 2]))