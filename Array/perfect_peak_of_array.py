# https://www.interviewbit.com/problems/perfect-peak-of-array/


# O(N) : prefix-suffix array => optimal but can be simplified
class Solution1:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):

        max_prefix = [0] * len(A)
        min_suffix = [0] * len(A)

        max_prefix[0] = A[0]
        min_suffix[len(A)-1] = A[len(A)-1]

        for i in range(1, len(A) - 1):
            max_prefix[i] = max(max_prefix[i-1], A[i])
        
        for i in range(len(A) - 2, 0, -1):
            min_suffix[i] = min(min_suffix[i+1], A[i])

        found = -1
        for i in range(1, len(A) - 1):
            if max_prefix[i] == min_suffix[i] and max_prefix[i] == A[i]:
                found = A[i]

        if found == -1:
            return 0
        else:
            count = 0
            for i in range(len(A)):
                if A[i] == found:
                    count += 1
            if count == 1:
                return 1
            else:
                return 0 

# O(N) : prefix-suffix array => better that 1st, eliminating unecesary checks
class Solution2:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):

        max_prefix = [0] * len(A)
        min_suffix = [0] * len(A)

        max_prefix[0] = A[0]
        min_suffix[len(A)-1] = A[len(A)-1]

        for i in range(1, len(A) - 1):
            max_prefix[i] = max(max_prefix[i-1], A[i-1])
        
        for i in range(len(A) - 2, 0, -1):
            min_suffix[i] = min(min_suffix[i+1], A[i+1])

        found = None
        for i in range(1, len(A) - 1):
            if max_prefix[i] < A[i] and A[i] < min_suffix[i]:
                found = A[i]
        
        if found == None:
            return 0
        else:
            return 1

# O(N) : prefix-suffix array => most efficient, using only 2 loops
class Solution3:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):

        max_prefix = [0] * len(A)
        min_suffix = [0] * len(A)

        max_prefix[0] = A[0]
        min_suffix = A[-1]

        for i in range(1, len(A) - 1):
            max_prefix[i] = max(max_prefix[i-1], A[i-1])
        
        for i in range(len(A) - 2, 0, -1):
            min_suffix = min(min_suffix, A[i+1])
            if max_prefix[i] < A[i] and A[i] < min_suffix:
                return 1
        return 0