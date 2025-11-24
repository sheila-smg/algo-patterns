"""
Longest Substring Without Repeating Characters (variable window)

Given a string s, return the length of the longest contiguous substring 
that contains no repeating characters.

Pattern: sliding window (variable-size)
"""

def length_of_longest_substring(s):
    char_index_map = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  
    print(length_of_longest_substring("bbbbb"))     
    print(length_of_longest_substring("pwwkew"))    