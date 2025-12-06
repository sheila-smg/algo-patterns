"""
Find Minimum in Rotated Sorted Array

You are given a sorted array that has been rotated at an unknown pivot.
All elements are distinct.

Return the minimum element in the array.

The minimum value is the point where the rotation occurred. Use binary
search by comparing the middle element with the right boundary to decide
which half contains the minimum.

"""

def find_min_rotated_sorted_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]

if __name__ == "__main__":
    print(find_min_rotated_sorted_array([3,4,5,1,2]))  # Output: 1
    print(find_min_rotated_sorted_array([4,5,6,7,0,1,2]))  # Output: 0
    print(find_min_rotated_sorted_array([11,13,15,17]))  # Output: 11