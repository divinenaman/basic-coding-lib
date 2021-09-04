
def permute(n,k):

	dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

	for i in range(n+1):
		for j in range(min(i,k) + 1):
			if j==0:
				dp[i][j] = 1
			else:
				dp[i][j] = dp[i-1][j] + (j*dp[i-1][j-1])

	return dp[n][k] 


n = int(input())
t = int(input())

ans = permute(n,t)

print(ans,end="\n")