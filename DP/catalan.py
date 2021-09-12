#https://www.geeksforgeeks.org/program-nth-catalan-number/

import nCr

# O(n)
# c(n) = (2nCn)/(n+1)
def catalan2(n):
	c = nCr.bioCoeff(2*n,n)
	return c/(n+1)

# O(n^2) 
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
ans1 = catalan(n)
ans2 = catalan2(n)
print(ans1,ans2,end="\n")