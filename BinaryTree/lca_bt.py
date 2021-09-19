# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getDepths(self,root,d,p,adj):
        if root != None:
            adj[root.val] = (p,root,d)
            self.getDepths(root.left,d+1,root.val,adj)
            self.getDepths(root.right,d+1,root.val,adj)
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2x
        # 2x + 1
        
        # bfs add depth
        adj = {}
        self.getDepths(root,0,None,adj)
                
        l = p.val
        k = q.val
        while True: 
            p1,n1,d1 = adj[l]
            p2,n2,d2 = adj[k]
            if l == k:
                return n1
            elif d1 < d2:
                k = p2
            elif d1 > d2:
                l = p1
            else:
                l = p1
                k = p2
                