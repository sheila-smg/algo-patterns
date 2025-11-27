"""
Given a string s and an integer k, return the length of the longest substring
that contains at most k distinct characters.
Use the sliding window pattern with a frequency dictionary.
The window grows by expanding the right pointer, and shrinks when the number
of distinct characters becomes greater than k.

"""

from collections import defaultdict

def longest_substring_with_k_distinct(s, k):
    window_frequency = defaultdict(int)
    left = 0
    max_length = 0
    for right in range(len(s)):
        right_char = s[right]
        window_frequency[right_char] += 1
        while len(window_frequency) > k:
            left_char = s[left]
            window_frequency[left_char] -= 1
            if window_frequency[left_char] == 0:
                del window_frequency[left_char]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

if __name__ == "__main__":
    s = "arrrraaci"
    k = 2
    print(longest_substring_with_k_distinct(s, k))