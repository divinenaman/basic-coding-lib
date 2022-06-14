# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        
        if len(A) == 1:
            return A[0]
        
        B = [0] * len(A)
        if A[0] > 0:
            B[0] = A[0]

        s = A[0]

        for i in range(1, len(A)):
            B[i] = B[i-1] + A[i]

            s = max(s, B[i])

            if B[i] < 0:
                B[i] = 0
        
        return s

o = Solution()

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(o.maxSubArray(A))