# https://leetcode.com/problems/majority-element/


"""
1. use a count and index variable
2. traverse through array
3. increment count if element at index and at looping variable is same
4. if elements are not same, 2 conditions arrise
5. if count > 0, decrement count
6. if count = 0, set index variable to current looping index and count to 1
7. the index stored in index is cadidate majority number
8. after loop ends, check if the cadidate majority number has len > n/2 

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        idx = 0
        
        for i in range(len(nums)):
            
            if nums[i] == nums[idx]:
                count += 1
            
            elif count > 0:
                count -= 1
            
            else:
                count = 1
                idx = i
        
        c = 0
        for i in range(len(nums)):
            if nums[idx] == nums[i]:
                c+=1
        
        return nums[idx]