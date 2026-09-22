# Problem: Longest Palindromic Substring
#
# Given a string s, return the longest palindromic substring.
# A palindrome is a string that reads the same forward and backward.
#
# Example:
# Input:  "babad"
# Output: "bab"
#
# Explanation:
# "bab" is the longest palindromic substring.
# "aba" is also a valid answer.

def longest_palindrome(s):
    if len(s) < 2:
        return s
    start = 0
    end = 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    for i in range(len(s)):

        # Odd-length palindrome
        left1, right1 = expand(i, i)

        # Even-length palindrome
        left2, right2 = expand(i, i + 1)

        if right1 - left1 > end - start:
            start = left1
            end = right1

        if right2 - left2 > end - start:
            start = left2
            end = right2
    return s[start:end + 1]

s = "babad"
print(longest_palindrome(s))

