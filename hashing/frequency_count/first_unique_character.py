"""
First Unique Character in a String

Given a string `s`, return the index of the **first non-repeating character**.
If no such character exists, return -1.

Examples:
- s = "leetcode" -> 0       ('l' is the first unique character)
- s = "loveleetcode" -> 2   ('v' is the first unique character)
- s = "aabb" -> -1

Goal:
Use a frequency map to count how many times each character appears.
Then scan the string again to find the first index with count == 1.

Constraints:
- 1 <= len(s)
- s consists of lowercase English letters.

"""

def first_unique_character(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1

if __name__ == "__main__":
    print(first_unique_character("leetcode"))       # Output: 0
    print(first_unique_character("loveleetcode"))   # Output: 2
    print(first_unique_character("aabb"))           # Output: -1
    print(first_unique_character("swiss"))          # Output: 0
    print(first_unique_character("racecar"))        # Output: 0