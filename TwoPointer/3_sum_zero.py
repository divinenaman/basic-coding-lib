# https://www.interviewbit.com/problems/3-sum-zero/

# simple application of 2 pointers on sorted array
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def threeSum(self, A):

        A.sort()
        sol = []

        if len(A) == 0:
            return []

        for i in range(len(A)):
            if i!=0 and A[i] <= A[i-1]:
                continue

            l = i + 1
            h = len(A) - 1

            while l < h:
                curr = A[l] + A[h] + A[i]

                if curr > 0:
                    h -= 1
                elif curr < 0:
                    l += 1
                else:
                    sol.append((A[i], A[l], A[h]))
                    l += 1
                    h -= 1
                    while l < h and A[l] == A[l-1]:
                        l += 1
                    while l < h and A[h] == A[h+1]:
                        h -= 1

        return sol