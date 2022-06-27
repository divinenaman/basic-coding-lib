# https://www.interviewbit.com/problems/kth-smallest-element-in-tree/


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	
    def getInorder(self, A, arr):
        if A:
            self.getInorder(A.left, arr)
        
            arr.append(A.val)
        
            self.getInorder(A.right, arr)
        
            
    def kthsmallest(self, A, B):
        
        stack = []
        
        self.getInorder(A.left, stack)
        
        stack.append(A.val)
        
        if len(stack) < B:
            self.getInorder(A.right, stack)
        
        return stack[B-1]
