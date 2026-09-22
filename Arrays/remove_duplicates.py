# Problem: Remove Duplicates from a Sorted Array
#
# Given a sorted array, remove the duplicate elements
# in-place so that each element appears only once.
#
# Example:
# Input:  [1, 1, 2, 2, 3, 4, 4]
# Output: [1, 2, 3, 4]
#
# Explanation:
# The array is already sorted, so we can use two pointers
# to keep track of unique elements.

def remove_duplicates(nums):
    if not nums:
        return 0
    position = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[position] = nums[i]
            position += 1
    return position

nums = [1, 1, 2, 2, 3, 4, 4]
k = remove_duplicates(nums)
print(nums[:k])
