# Problem: Two Sum
# Description - 
# Given an array of integers nums and an integer target,
# return the indices of the two numbers whose sum is equal
# to the target.
#
# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
#
# Explanation:
# nums[0] + nums[1] = 2 + 7 = 9

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
