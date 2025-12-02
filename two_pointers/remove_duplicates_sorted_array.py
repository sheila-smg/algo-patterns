"""
    Remove duplicates from a sorted array in-place using the two pointers pattern.

    The function modifies the input list so that the first part contains the
    unique elements in their original relative order. Elements beyond the returned
    length are unspecified. The operation is done in-place with O(1) extra space.

"""

def remove_duplicates_sorted_array(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return nums[:slow + 1]

if __name__ == "__main__":
    print(remove_duplicates_sorted_array([0, 1, 1, 2, 2, 3, 4, 4,5]))