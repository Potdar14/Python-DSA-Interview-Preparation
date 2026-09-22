# Problem: Reverse an Array
#
# Given an array of integers, reverse the array in-place.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
# Explanation:
# The first element becomes the last,
# the second becomes the second-last, and so on.

def reverse_array(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

nums = [1, 2, 3, 4, 5]
print(reverse_array(nums))
