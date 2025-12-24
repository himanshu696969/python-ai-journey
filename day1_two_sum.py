# LeetCode: Two Sum
# Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            return []
