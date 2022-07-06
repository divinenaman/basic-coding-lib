# https://www.interviewbit.com/problems/disjoint-intervals/

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        sorted_int = sorted(A, key=lambda x: x[1])
        
        interval = sorted_int[0]
        i = 1
        c = 1
        while i < len(A):
            
            if sorted_int[i][0] > interval[1]:
                interval[0] = min(sorted_int[i][0], interval[0])
                interval[1] = max(sorted_int[i][1], interval[1])
                c+=1
            i+=1
        
        return c