# Problem: Valid Palindrome
#
# Given a string, determine whether it is a palindrome,
# considering only alphanumeric characters and ignoring case.
#
# Example:
# Input:  "A man, a plan, a canal: Panama"
# Output: True
#
# Explanation:
# After removing spaces and special characters:
# "amanaplanacanalpanama"
# This reads the same forward and backward.

def is_palindrome(s):
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]
s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
