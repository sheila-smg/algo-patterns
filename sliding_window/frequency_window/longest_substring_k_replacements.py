"""
Given a string s and an integer k, return the length of the longest substring
that can be turned into a string of identical characters by replacing at most
k characters.

Use a sliding window with character frequencies. Track the count of the most
frequent character in the window. The window is valid while:
    window_size - max_freq <= k

Shrink from the left when invalid. Compute the max valid window size.
"""

from collections import defaultdict

def longest_substring_k_replacements(s, k):
    left = 0
    max_length = 0
    char_count = defaultdict(int)
    max_freq = 0

    for right in range(len(s)):
        char_count[s[right]] += 1
        max_freq = max(max_freq, char_count[s[right]])

        while (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    s = "AABABBA"
    k = 2
    print(longest_substring_k_replacements(s, k))