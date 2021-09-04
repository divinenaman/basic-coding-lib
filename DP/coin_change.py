
# https://practice.geeksforgeeks.org/problems/coin-change2448/1

def calCoinChange(n,a):

	dp = [0]*(n+1)
	dp[0] = 1

	for i in a:
		for j in range(len(dp)):
			if i <= j:
				dp[j]+=dp[j-i]
	return dp[n]
				
n = int(intput())
m = int(input())
a = list(map(int,input().split()))

total_ways = calCoinChange(n,a)

print(total_ways,end='\n')
