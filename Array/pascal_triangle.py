# https://www.interviewbit.com/problems/pascal-triangle/

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A <= 0:
            return []
            
        triangle = [[1]]
        for i in range(1, A):
            row = []
            for j in range(i+1):
                s = 0
                if 0 <= j and j < i:
                    s += triangle[i-1][j]
                if 0 <= j-1 and j-1 < i:
                    s += triangle[i-1][j-1]
                
                row.append(s)

            triangle.append(row)
        
        return triangle