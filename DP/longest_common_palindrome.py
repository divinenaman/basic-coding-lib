class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        n = len(A)
        
        dp = [[0 for i in range(n+2)] for i in range(n+1)]
        
        i = 0
        maxx = 0
        
        while i <= n:
            j = n
            while i <= j:
                if i == 0 or j == 0:
                    dp[i][j] = 0

                elif A[i - 1] == A[j - 1]:
                    
                    dp[i][j] = dp[i-1][j+1]

                    if i == j:
                        dp[i][j]+=1
                    else:
                        dp[i][j]+=2

                    maxx = max(dp[i][j], maxx)
                      
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i-1][j])
                j -= 1
            i+=1  
        # for i in dp:
        #     print(i)        
        
        return maxx       


o = Solution()

s = "bebdeeedaddecebbbbbabebedc"

s = "aba"

s = "cbbcacdcdadc"

print(o.solve(s))
