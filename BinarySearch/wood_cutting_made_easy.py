# https://www.interviewbit.com/problems/woodcutting-made-easy/


"""

search for answer instead of iterating through one by one.

"""

class Solution:     
    def solve(self, A, B):
        
        max_height = 0
        
        l = 0
        h = 10**7
        
        while l<=h:
            
            mid = (l + h)//2
            
            recieved = sum([i - mid for i in A if i > mid])
                
            if recieved < B:
                h = mid - 1
                
            else:
                l = mid + 1
                max_height = max(max_height, mid)
        
        return max_height