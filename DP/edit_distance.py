import sys

def edit_distance(a,b):
    n = len(a)
    m = len(b)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1,m + 1):
        c = b[i - 1]
        for j in range(1,n + 1):
            if c == a[j - 1]:            
                dp[i][j] = dp[i-1][j-1]      
            else:
                dp[i][j] = dp[i-1][j-1] + 1
    
    minn = sys.maxsize
    for i in range(1,m):
        minn = min(minn, dp[i][n] + m - i )
    
    return minn

str1 = "sunday"
str2 = "saturday"
ans = edit_distance(str1, str2)

print(ans,end='\n')