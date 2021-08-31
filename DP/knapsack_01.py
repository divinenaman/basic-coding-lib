
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

def knapsack01(w,n,wt,val):
	dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

	for i in range(n+1):
		for j in range(w+1):
			if i == 0 or j == 0:
				dp[i][j] = 0
			elif wt[i-1] <= j:
				dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
			else:
				dp[i][j] = dp[i-1][j]
    return dp[n][w]
				
w = int(intput())
m = int(input())
wt = list(map(int,input().split()))
val = list(map(int,input().split()))

max_val = knapsack01(w,m,wt,val)

print(max_val,end='\n')
