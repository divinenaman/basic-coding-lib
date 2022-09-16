
# https://codeforces.com/blog/entry/105455?#comment-938269

a = [1,0,0,1,1,0,1,1,0,1,1,0,0]

# ration of 0's to 1's should be x:y
x = 1
y = 4

prefix = [0] * len(a) + 1
freq = {}

for i in range(1, len(a) + 1):
    if a[i] == 0:
        v = x
    else:
        v = -y
    
    prefix[i] = prefix[i-1] + v

    if prefix[i] in freq:
        freq[prefix[i]] += 1
    else:
        freq[prefix[i]] = 1

ans = 0

for i in freq:
    ans += (freq[i] * (freq[i] - 1)) // 2


print(ans)