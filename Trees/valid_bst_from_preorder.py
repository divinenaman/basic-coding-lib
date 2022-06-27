# https://www.interviewbit.com/problems/valid-bst-from-preorder/

class ConstructTree:        
    def __init__(self):
        self.idx = 0
        self.tree = set()
    
    def checkPreorder(self, pre, size, min_val, max_val):
        if pre[self.idx] == min_val or pre[self.idx] == max_val:
            return
        
        if pre[self.idx] > min_val and pre[self.idx] < max_val:
            
            val = pre[self.idx]
            self.tree.add(val)

            self.idx += 1
            
            if self.idx < size:
                self.checkPreorder(pre, size, min_val, val)
                    
            if self.idx < size:
                self.checkPreorder(pre, size, val, max_val)

                
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        tree = ConstructTree()
        
        tree.checkPreorder(A, len(A), float('-inf'), float('inf'))
            
        if len(tree.tree) == len(A):
            return 1
        else:
            return 0 


A = [ 197, 74, 48, 6, 23, 93, 98, 146, 110, 919, 357, 247, 278, 267, 270, 775, 469, 436, 390, 412, 464, 458, 681, 629, 622, 503, 611, 583, 644, 705, 686, 702, 721, 759, 811, 830, 872, 902, 985, 961, 933, 994 ]

A = [ 315, 279, 263, 205, 187, 184, 70, 68, 141, 100, 176, 185, 193, 309, 839, 749, 491, 384, 364, 416, 392, 386, 418, 417, 457, 433, 655, 645, 596, 584, 524, 630, 748, 667, 658, 692, 735, 732, 805, 787, 773, 763, 763, 796, 897, 896, 859, 863, 886, 960, 948, 943, 969, 996, 989 ]


o = Solution()

print(o.solve(A))