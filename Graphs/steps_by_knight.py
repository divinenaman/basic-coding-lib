import sys

def isSafe(a,b,n):
	if (a<n and b<n and a>-1 and b>-1):
		return True
	else:
		return False

def solve(n,s1,s2,d1,d2):
	visited = [[False for _ in range(n)] for _ in range(n)]
	steps = bfs_to_target(n,s1,s2,d1,d2)
	print("ans",steps,end='\n')

def bfs_to_target(n,s1,s2,d1,d2):
	queue = []
	visited = [[False for _ in range(n)] for _ in range(n)]
	queue.append((s1,s2,0))

	while len(queue) > 0:
		s1,s2,dist = queue[0]
		queue.pop(0)

		t,d,l,r = s1 + 2,s1 - 2,s2 - 2,s2 + 2
		w,x,y,z = s2 + 1, s2 - 1,s1 + 1,s1 - 1
	
		if s1 == d1 and s2 == d2:
			return dist

		if not visited[s1][s2]:
			visited[s1][s2] = True

			if isSafe(t,w,n):
				queue.append((t,w,dist+1))
			if isSafe(t,x,n):
				queue.append((t,x,dist+1))
			if isSafe(d,w,n):
				queue.append((d,w,dist+1))		
			if isSafe(d,x,n):
				queue.append((d,x,dist+1))
			if isSafe(l,y,n):
				queue.append((l,y,dist+1))
			if isSafe(l,z,n):
				queue.append((l,z,dist+1))				
			if isSafe(r,y,n):
				queue.append((r,y,dist+1))
			if isSafe(r,z,n):
				queue.append((r,z,dist+1))	
			
	return -1		

n = 6
s1,s2 = [4,5]
d1,d2 = [1,1]

print(n,s1,s2,d1,d2)

solve(n,s1,s2,d1,d2)