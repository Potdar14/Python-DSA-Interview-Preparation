# Problem: Valid Anagram
#
# Given two strings s and t, determine whether t is an anagram of s.
#
# Example:
# Input:
# s = "anagram"
# t = "nagaram"
# Output: True

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    return True

s = "anagram"
t = "nagaram"
print(is_anagram(s, t))

