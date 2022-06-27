# https://www.interviewbit.com/problems/container-with-most-water/

"""

Notice whenever there is a condition where 
answer depends on min or max of 2 values and 
the position of the element (in the array) cannot be changed,
the required value can be computed by moving one of the 2 pointers 
in O(N) time complexity.

"""
class Solution:
	# @param A : list of integers
	# @return an integer
	def maxArea(self, A): 
        i = 0
        j = len(A) - 1
        maxx = 0
        
        while i < j:
            if A[i] <= A[j]:
                maxx = max(maxx, A[i] * (j-i))
                i+=1
            else:
                maxx = max(maxx, A[j] * (j-i))
                j-=1
        return maxx