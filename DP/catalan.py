



# c(1) = 1 && c(n+1) = sum(c(i)*c(n-1), i=0 to n))
def catalan(n):
	if n==0 or n==1:
		return 1
	dp = [0 for _ in range(n+1)]

	dp[0] = 1
	dp[1] = 1
	for i in range(2,n+1):
		for j in range(i):
			dp[i]+=dp[j]*dp[i-j-1]
	return dp[n]

n = int(input())
ans = catalan(n)
print(ans,end="\n")