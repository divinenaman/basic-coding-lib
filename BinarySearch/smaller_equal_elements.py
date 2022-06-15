# https://www.interviewbit.com/problems/smaller-or-equal-elements/


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def find_target(self, A, l, h, t):
        
        if l <= h:
            
            mid = (l+h)//2
            
            if A[mid] > t:
                
                if A[mid-1] <= t:
                    return mid - 1
                
                h = mid - 1
            
            else:
                if mid + 1 > h:
                    return h
                    
                l = mid + 1
        
            return self.find_target(A, l, h, t)
            
        return -1
    
    def solve(self, A, B):
        
        idx = self.find_target(A, 0, len(A) - 1, B)
        
        return idx + 1