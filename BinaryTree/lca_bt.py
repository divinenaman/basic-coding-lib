# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution1:
    """
        Time: O(N)
        Space: O(N)
        Runtime: 74ms (leetcode)
    """
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def recurse(curr_node):
            left = recurse(curr_node.left)
            right = recurse(curr_node.right)
            mid = p == curr_node or q == curr_node

            if mid + left + right >= 2:
                self.ans = curr_node
            
            return mid or left or right

        recurse(root)
        return self.ans

class Solution2:
    """
        Time: O(N)
        Space: O(N)
        Runtime: 64ms (leetcode)
    """
    
    def getDepths(self,root,d,p,adj):
        if root != None:
            adj[root.val] = (p,root,d)
            self.getDepths(root.left,d+1,root.val,adj)
            self.getDepths(root.right,d+1,root.val,adj)
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
                