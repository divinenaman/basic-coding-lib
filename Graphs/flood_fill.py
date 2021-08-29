def isSafe(a,b,n,m):
	return a<n and b<m and a>-1 and b>-1 

def fill_using_bfs(a,n,m,s1,s2,c):
	queue = []
	target = a[s1][s2]
	steps = [1,-1]
	queue.append((s1,s2))
	visited = [[False for _ in range(m)] for _ in range(n)]

	while len(queue) > 0:
		s1,s2 = queue[0]
		queue.pop(0)

		if isSafe(s1,s2,n,m) and a[s1][s2] == target:
			a[s1][s2] = c 
			visited[s1][s2] = True

			for i in steps:
				if isSafe(s1+i,s2,n,m) and visited[s1+i][s2] == False :
					queue.append((s1+i,s2))
				if isSafe(s1,s2+i,n,m) and visited[s1][s2+i] == False :	
					queue.append((s1,s2+i))
		
	return a					

n = int(input())
m = int(input())

a = []

for i in range(n):
	a.append(list(map(int,input().split())))

s1 = 1
s2 = 1
c = 1

a = fill_using_bfs(a,n,m,s1,s2,c)

print(a)