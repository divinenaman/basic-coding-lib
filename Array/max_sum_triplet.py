# https://www.interviewbit.com/problems/maximum-sum-triplet/

from bisect import bisect_left

# O(n*2) solution:  On analysing this methods make unecessary triplets which is not required, 
# the fact that triplet is in increasing order allows us to eleminate triplets
class Solution1:
    def solve(self, A):      
        rightmost = [-1]*len(A)
        leftmost = [-1]*len(A)  
        
        for i in range(len(A) - 2, -1, -1):
            t = -1
            for j in range(i + 1, len(A)):
                t = max(t, A[j])
                if t > A[i] and t > rightmost[i]:
                    rightmost[i] = t

        for i in range(1, len(A) - 1):
            t = -1
            for j in range(0, i):
                if A[j] < A[i] and A[j] > leftmost[i]:
                    leftmost[i] = A[j]
        s = 0
        for i in range(0, len(A)):
            if rightmost[i] != -1 and leftmost[i] != -1:
                s = max(s, leftmost[i] + A[i] + rightmost[i])
        
        return s


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return i - 1
    else:
        return -1

# O(NLogN) Solution: max suffix array to get leftmost element and binary search to get get rightmost elment.
class Solution2:
    def solve(self, A):      
        leftmost = [0]*len(A)  
        leftmost[len(A) - 1] = A[-1]
        # i-th index gives largest value between [i, len(A)]
        for i in range(len(A) - 2, -1, -1):
            leftmost[i] = max(A[i], leftmost[i+1])

        rightmost = [A[0]]
        s = 0

        for i in range(1, len(A) - 1):
            res = BinarySearch(rightmost, A[i])
            if res != -1 and leftmost[i+1] > A[i]:
                s = max(s, rightmost[res] + A[i] + leftmost[i+1])
            rightmost.insert(res+1, A[i])  
        return s


sol = Solution2()
#A = [ 154, 293, 12383, 17422, 18717, 19719, 19896, 5448, 21727, 14772, 11539, 1870 ]
A = [ 32592, 18763, 1656, 17411, 6360, 27625, 20538, 21549, 6484, 27596 ]

print(sol.solve(A))
