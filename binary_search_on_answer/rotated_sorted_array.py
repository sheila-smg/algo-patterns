"""
Search in Rotated Sorted Array

You are given a sorted array that has been rotated at an unknown pivot.
All elements are distinct.

Return the index of the target if it exists in the array, otherwise
return -1.

At least one side of the array (left or right) is always sorted. Use
this property to decide which half to continue searching.

"""

def search_rotated_sorted_array(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]: # Left side is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # Right side is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

if __name__ == "__main__":
    print(search_rotated_sorted_array([4,5,6,7,0,1,2], 0))  # Output: 4
    print(search_rotated_sorted_array([4,5,6,7,0,1,2], 3))  # Output: -1
    print(search_rotated_sorted_array([1], 0))              # Output: -1