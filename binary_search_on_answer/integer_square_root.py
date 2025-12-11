"""
Integer Square Root

Given a non-negative integer n, return the integer part of its square
root (i.e. the floor of sqrt(n)). Do not use any built-in square root
functions.

This problem applies binary search on the answer space, using the
monotonic property that if x * x <= n, all values smaller than x also
satisfy the condition.
"""

def integer_square_root(n):
    if n < 2:
        return n

    left = 1
    right = n // 2
    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        mid_squared = mid * mid

        if mid_squared == n:
            return mid
        elif mid_squared < n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

if __name__ == "__main__":  
    print(integer_square_root(16))  # Output: 4
    print(integer_square_root(20))  # Output: 4
    print(integer_square_root(0))   # Output: 0
    print(integer_square_root(1))   # Output: 1
    print(integer_square_root(25))  # Output: 5