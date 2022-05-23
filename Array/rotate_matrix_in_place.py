class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        m = len(A[0])

        max_ele = 0

        for i in A:
            max_ele = max(max_ele, max(i))
        max_ele += 1
        
        for i in range(n):
            for j in range(m):
                if A[i][j] < max_ele:
                    A[i][j] *= max_ele
                if A[j][m - i - 1] < max_ele:
                    A[j][m - i - 1] *= max_ele
                
                A[j][m - i - 1] += A[i][j] // max_ele

        for i in range(n):
            for j in range(m):
                A[i][j] %= max_ele      

A = [[1,2,3], [4,5,5], [4,21,22]]

o = Solution()

o.rotate(A)

print(A)
