class Solution1:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        diagonals = []
        for i in range(len(A)):
            n = 0
            m = i
            row = []
            while n < len(A) and m >= 0:
                row.append(A[n][m])
                n += 1
                m -= 1
            diagonals.append(row)

        for j in range(1, len(A)):
            n = j
            m = len(A) - 1
            row = []
            while n < len(A) and m >= 0:
                row.append(A[n][m])
                n += 1
                m -= 1
            diagonals.append(row)

        return diagonals

# as row index increases and col index decreased, the sum remains constant 
class Solution2:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n=len(A)
        ans=[[] for i in range(2*n-1)]
        for i in range(n):
            for j in range(n):
                ans[i+j].append(A[i][j])
        return ans

o = Solution1()

A = [[1,2,4], [4,5,6], [7,8,9]]

print(o.diagonal(A))