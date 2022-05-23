# https://www.interviewbit.com/problems/sort-array-with-squares/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        arr = [0] * len(A)

        i = 0
        j = len(A) - 1
        c = len(A) - 1
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                arr[c] = A[i]**2
                i+=1
            else:
                arr[c] = A[j]**2
                j-=1
            c-=1
        
        return arr



