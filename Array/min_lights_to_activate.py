# https://www.interviewbit.com/problems/minimum-lights-to-activate/

class Solution:
    def solve(self, A, B):
        corridor = 1
        f = 0
        arr = []
        for i in range(len(A)):
            k = A[i]
            if k == 1:
                light_range = (i+1-B+1, i+1+B-1)

                if light_range[0] <= corridor:
                    
                    pop = 0
                    while len(arr) > 0 and arr[-1][0] >= light_range[0]:
                        pop += 1
                        corridor = arr[-1][0]
                        arr.pop()
                      
                    f -= pop
                    f += 1
                    arr.append((corridor, light_range[1]))
                    corridor = light_range[1] + 1
            if corridor > len(A):
                return f
        
        if corridor > len(A):
            return f
        else:
            return -1

A = [ 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0 ]
B = 12

A = [ 1, 1, 1, 1 ]
B = 3

o = Solution()
print(o.solve(A, B))