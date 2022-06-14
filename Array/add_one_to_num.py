# https://www.interviewbit.com/problems/add-one-to-number/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 0

        j = 0
        while j < len(A) and A[j] == 0:
            j += 1

        if j >= len(A):
            A = [0]
        else:
            A = A[j:]

        s = (A[-1] + 1) % 10
        carry = (A[-1] + 1) // 10

        A[-1] = s

        for i in range(len(A) - 2, -1, -1):
            if carry == 0:
                break
            else:
                s = (A[i] + carry) % 10
                carry = (A[i] + carry) // 10
                A[i] = s
        
        if carry == 0:
            return A
        else:
            return [carry] + A

A = [0, 0, 0, 1, 2, 3]

o = Solution()

print(o.plusOne(A))