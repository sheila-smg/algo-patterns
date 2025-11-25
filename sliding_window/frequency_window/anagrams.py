"""
Given two strings s and p, return all starting indices of substrings in s that are anagrams of p.

Two strings are anagrams if they use the same characters with the same frequencies. 
The goal is to slide a window of size len(p) over s and compare its frequency map with the frequency map of p. 
Every time both maps match, the starting index of the window is added to the result.
Pattern: sliding window (frequency-based)"""

from collections import defaultdict



def find_anagrams(s, p):

    p_frequency = defaultdict(int)
    window_frequency = defaultdict(int)
    result_indices = []
    p_length = len(p)
    
    for char in p:
        p_frequency[char] += 1
        
    left = 0
    
    for right in range(len(s)):
        right_char = s[right]
        window_frequency[right_char] += 1
        
        if right >= p_length:
            left_char = s[left]
            window_frequency[left_char] -= 1
            if window_frequency[left_char] == 0:
                del window_frequency[left_char]
            left += 1
            
        if window_frequency == p_frequency:
            result_indices.append(left)
            
    return result_indices

if __name__ == "__main__":
    s = "cbabcbabacd"
    p = "abc"
    print(find_anagrams(s, p))
