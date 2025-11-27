"""
Given two strings s and t, return the smallest substring of s that contains
all the characters of t (including multiplicities). If no such substring
exists, return an empty string "".

Use the sliding window pattern with a frequency dictionary for the target
string t and another for the current window in s.

Expand the right pointer to include characters until the window contains all
characters required by t, then shrink from the left to find the minimum size
window that still satisfies the requirement.
"""

from collections import defaultdict

def min_window_substring(s, t):

    t_frequency = defaultdict(int)
    window_frequency = defaultdict(int)
    have, need = 0, len(set(t))
    left = 0
    min_length = len(s) + 1
    min_window = ""
    for char in t:
        t_frequency[char] += 1

    for right in range(len(s)):
        right_char = s[right]
        window_frequency[right_char] += 1
        if right_char in t_frequency and window_frequency[right_char] == t_frequency[right_char]:
            have += 1
        while have == need:
            window_size = right - left + 1
            if window_size < min_length:
                min_length = window_size
                min_window = s[left:right + 1]
            left_char = s[left]
            window_frequency[left_char] -= 1
            if left_char in t_frequency and window_frequency[left_char] < t_frequency[left_char]:
                have -= 1
            left += 1

    return min_window

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(min_window_substring(s, t))







