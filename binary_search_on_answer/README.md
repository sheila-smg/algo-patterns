# Binary Search

Binary Search is an algorithm for efficiently locating an element in a sorted array.  
It works by repeatedly dividing the search interval in half until the target is found or the interval becomes empty.

## How it works

1. Set two pointers: 'left' and 'right'.
2. Compute 'mid = left + (right - left) // 2'.
3. Compare 'nums[mid]' with the target.
4. Adjust the search boundaries.
5. Stop when 'left > right'.

Time complexity: **O(log n)**  
Space complexity: **O(1)**

## Iterative implementation

"""
python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
"""

## Why this mid formula

Using `(left + right) // 2` can overflow in languages with fixed integer sizes.  
The safe version avoids adding two potentially large integers:

```
mid = left + (right - left) // 2
```

## Common variations

### First and Last Occurrence
Find the first or last index of a repeated value.

### Rotated Sorted Array
One half is always sorted. Use that to decide the direction.

### Peak Element
Find a peak in an array that increases then decreases.

### Binary Search on Answer
Search for the minimum value `x` that satisfies a condition.

## Repository structure

```
binary_search/
    README.md
    binary_search.py
    first_last_occurrence.py
    rotated_binary_search.py
    binary_search_on_answer.py
```

## Usage

```python
from binary_search import binary_search

nums = [1, 3, 5, 6, 8, 10]
print(binary_search(nums, 6))
```
