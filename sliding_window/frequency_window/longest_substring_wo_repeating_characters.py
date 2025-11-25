"""
Longest Substring Without Repeating Characters (frequency window)

Given a string s, find the length of the longest substring that contains no repeated characters.

This problem uses the frequency-based sliding window pattern. 
The window expands to include new characters and contracts whenever a character becomes repeated. 
A frequency map tracks how many times each character appears inside the window. 
The goal is to maintain the largest possible window where all characters are unique.

"""

def longest_substring_wo_repeating_characters(s):
    char_frequency = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        right_char = s[right]
        char_frequency[right_char] = char_frequency.get(right_char, 0) + 1
        
        while char_frequency[right_char] > 1:
            left_char = s[left]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            left += 1
            
        max_length = max(max_length, right - left + 1)
        
    return max_length

if __name__ == "__main__":
    print(longest_substring_wo_repeating_characters("abcdefgabhijklmab"))
    print(longest_substring_wo_repeating_characters("abcdefghijklmnopa"))