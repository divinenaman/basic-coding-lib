# https://www.interviewbit.com/problems/flip/



# O(n) : kadane's algorithm
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        s = 0
        m = 0
        l = None
        r = None
        start = 0
        for j, i in enumerate(A):
            if i == '0':
                s += 1 
            else:
                s -= 1
            if s > m:
                l = start
                r = j
                m = s

            # s <= 0 does not maintain lexical ordering, s < 0 maintains lexical order
            if s < 0:
                start = j + 1
                s = 0 
        if l == None or r == None:
            return []
        
        else:
            return [l + 1,r + 1]

A = "010"

s = Solution()

print(s.flip(A))