# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        prev_mn = nums[0]
        prev_mx = nums[0]
        
        mx = prev_mx
        mn = prev_mn
        
        total = nums[0]
        
        for i in range(1, n):
            
            prev_mx = max(prev_mx + nums[i], nums[i])
            mx = max(prev_mx, mx)
            
            prev_mn = min(prev_mn + nums[i], nums[i])
            mn = min(prev_mn, mn)
            
            total += nums[i]
        
        if total - mn == 0:
            return mx
        
        else:
            return max(mx, total - mn)