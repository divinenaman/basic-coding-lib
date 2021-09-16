# https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

import sys

def matrix_chain_multiplication(arr,n):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for L in range(2,n):
        for i in range(1,n - L + 1):
            j = i + L - 1
            dp[i][j] = sys.maxsize
            for k in range(i,j):
                q = dp[i][k] + dp[k + 1][j] + arr[i-1]*arr[k]*arr[j]
                if q < dp[i][j]:
                    dp[i][j] = q
    return dp[1][n-1]

arr = [1,2,3,4]
n = 4
ans = matrix_chain_multiplication(arr,n)

print(ans,end='\n')