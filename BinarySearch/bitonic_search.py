class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def find_target_desc(self, A, l, h, t):
        if l <= h:
            mid = (l+h)//2
            
            if A[mid] == t:
                return mid
            
            elif t > A[mid]:
                h = mid - 1
            
            else:
                l = mid + 1
            
            return self.find_target_desc(A, l, h, t)
        
        return -1
    
    def find_target_asc(self, A, l, h, t):
        if l <= h:
            mid = (l+h)//2
            
            if A[mid] == t:
                return mid
            
            elif t > A[mid]:
                l = mid + 1
            
            else:
                h = mid - 1
            
            return self.find_target_asc(A, l, h, t)
        
        return -1
            
    def find_decreasing_trend(self, A, l, h):
        
        if l <= h:
            mid = (l+h)//2
            
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            
            elif A[mid-1] < A[mid]:
                l = mid + 1
            
            else:
                h = mid - 1
            
            return self.find_decreasing_trend(A, l, h)
        
        return len(A) - 1
        
    def solve(self, A, B):
        
        idx = self.find_decreasing_trend(A, 0, len(A)-1)
        exist = self.find_target_asc(A, 0, idx, B)

        #print(idx, exist)
        if exist != -1:
            return exist
        
        
        if idx < len(A) - 1:
            exist = self.find_target_desc(A, idx+1, len(A)-1, B)
            #print(exist)
            if exist != -1:
                return exist
        
        return -1
        
        
            
o = Solution()

A = [ 1, 2, 3, 4, 5, 10, 9, 8, 7, 6 ]
B = 5

A = [ 1, 20, 50, 40, 10 ]
B = 5

A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ]
B = 12

print(o.solve(A,B))