# https://www.interviewbit.com/problems/maximum-absolute-difference/

class Solution:
    def maxArr(self, A):
        maxx1 = A[0]
        maxx2 = A[0] 
        minn1 = A[0]
        minn2 = A[0]

        for i in range(1, len(A)):
            if A[i] + i > maxx1:
                maxx1 = A[i] + i
            
            if A[i] + i < minn1:
                minn1 = A[i] + i
            
            if A[i] - i > maxx2:
                maxx2 = A[i] - i
            
            if A[i] - i < minn2:
                minn2 = A[i] - i
        
        return max(maxx1 - minn1, maxx2 - minn2)