# https://leetcode.com/problems/two-sum/
# 60ms, faster than 78.65%

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dp.keys():
               return [i,dp[x]]
            else:
                dp[nums[i]] = i