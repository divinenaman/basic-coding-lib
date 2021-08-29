"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# leet-code

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        edge = None
        queue = [node]
        addrMap = {}
        visited = [False for _ in range(100)]
        while len(queue) > 0:
            curr = queue[0]
            queue.pop(0)
            nei = []
            if curr == None:
                continue
                
            temp = curr.neighbors
            if temp == None:
                temp = []
                
            for i in temp:
                if visited[i.val-1] == False:
                    queue.append(i)
                    visited[i.val-1] = True
                    
                if i.val in addrMap:
                    nei.append(addrMap[i.val])
                else:
                    addrMap[i.val] = Node(i.val)
                    nei.append(addrMap[i.val])
            if curr.val in addrMap:        
                addrMap[curr.val].neighbors = nei
            else:
                addrMap[curr.val] = Node(curr.val,nei)
            if edge==None:
                edge = addrMap[curr.val]
        return edge
        