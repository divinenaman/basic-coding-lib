# https://www.interviewbit.com/problems/3-sum/

# O(N^2): mostly N^3 problem requires N^2 solution
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        
        A.sort()

        i = 0
        close = float('inf')
        s = 0
        while i < len(A):
            l = i + 1
            h = len(A) - 1
            target = B - A[i]
            
            while l < h:
                curr = A[l] + A[h]
                                
                if abs(target - curr) < close:
                    close = abs(target - curr)
                    s = A[i] + A[l] + A[h]
                
                if target > curr:
                    l+=1
                else:
                    h-=1
            i+=1
        return s 