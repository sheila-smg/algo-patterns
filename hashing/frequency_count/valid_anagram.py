"""
Valid Anagram

Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
and False otherwise.

An anagram is a word or phrase formed by rearranging the letters of
another, using all original letters exactly once.

Examples:
- s = "anagram", t = "nagaram" -> True
- s = "rat", t = "car" -> False

Goal:
Use frequency counting (hash maps) to compare character occurrences
in O(n) time.

Constraints:
- 1 <= len(s), len(t)
- Strings consist of lowercase English letters or general ASCII characters.
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True

if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # Output: True
    print(is_anagram("rat", "car"))          # Output: False
    print(is_anagram("listen", "silent"))    # Output: True
    print(is_anagram("hello", "billion"))    # Output: False
    print(is_anagram("aabbcc", "abcabc"))    # Output: True
