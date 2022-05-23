# Log(N) and inplace
# first the first element which is in ascending order from n-1 to i
# if no such element return reverse of array
# else replace the found element at ith index with the smallest element just larger ith element with range (i+1, n-1)
# reverse elements in (i-1, n-1)   
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        n = len(A)    
        maxx = n-1
        idx = -1
        for i in range(n - 2, -1, -1):
            if A[i] < A[maxx]:
                idx = i
                break
            else:
                maxx = i

        if idx == -1:
            return A[::-1]

        else:
            min_max = -1
            for i in range(n-1, idx, -1):
                if A[i] > A[idx]: 
                    if min_max == -1:
                        min_max = i
                    
                    elif A[i] < A[min_max]:
                        min_max = i
                                
            A[idx], A[min_max] = A[min_max], A[idx]

            for i in range((n-idx) // 2):
                A[idx + 1 + i], A[n - 1 - i] = A[n - 1 - i], A[idx + 1 + i]

            return A 

# another sol, more efficient
# find 1st ascending trend
# find element just larger than element found above from n-1 to i+1
# replace the two elements
# reverse elements in range i+1, n-1
def next_permutation(L):
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i+1]:
        i -= 1
    if i == -1:
        return False
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
    L[i], L[j] = L[j], L[i]
    left = i + 1
    right = n - 1
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return True

A = [ 251, 844, 767, 778, 658, 337, 10, 252, 632, 262, 707, 506, 701, 475, 410, 696, 631, 903, 516, 149, 344, 101, 42, 891, 991 ]

A2 = [ 444, 994, 508, 72, 125, 299, 181, 238, 354, 223, 691, 249, 838, 890, 758, 675, 424, 199, 201, 788, 609, 582, 979, 259, 901, 371, 766, 759, 983, 728, 220, 16, 158, 822, 515, 488, 846, 321, 908, 469, 84, 460, 961, 285, 417, 142, 952, 626, 916, 247, 116, 975, 202, 734, 128, 312, 499, 274, 213, 208, 472, 265, 315, 335, 205, 784, 708, 681, 160, 448, 365, 165, 190, 693, 606, 226, 351, 241, 526, 311, 164, 98, 422, 363, 103, 747, 507, 669, 153, 856, 701, 319, 695, 52 ]

print(len(A2))

o = Solution()

print(o.nextPermutation(A2))