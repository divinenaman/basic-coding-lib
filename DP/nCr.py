# https://practice.geeksforgeeks.org/problems/ncr1019/1

def solve(n,r):
	if r > n:
		return 0

	dp = [[0 for i in range(n+1)] for _ in range(r+1)]

	for i in range(n+1):
		for j in range(min(i,r)+1)
		if i == 0 or j == 0:
			dp[i][j] = 1
		else:
			dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

	bio = int(dp[n][r]%(pow(10,9)+7))

	return bio

n = int(input())
r = int(input())

nCr = solve(n,r)

print(nCr,end='\n')