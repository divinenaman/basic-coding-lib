# AVL Trees
# https://www.hackerrank.com/challenges/self-balancing-tree/problem

class BST:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.ht = 0

def balanceFactor(node1,node2):
    h1 = 0
    h2 = 0
    if node1 != None:
        h1 = node1.ht + 1
    if node2 != None:
        h2 = node2.ht + 1
    return abs(h1-h2)     

def getHeight(node):
    if node != None:
        return node.ht + 1
    return 0

def rightRotate(node):
    # interchange value
    v1 = node.val
    node.val = node.left.val
    node.left.val = v1
    
    # get left node (with interchanged value, target is to make it right child of root)
    old_left_child = node.left
    
    # set root's left child to root's left child's left child 
    node.left = node.left.left
    
    # interchange root's old left child children (why we don't need left child, it's now the left child of root [line-35])
    old_left_child.left = old_left_child.right
    
    old_left_child.right = node.right
    node.right = old_left_child

    # Height Recal
    node.right.ht = max(getHeight(node.right.right),getHeight(node.right.left))
    node.ht = max(getHeight(node.left),getHeight(node.right))

def leftRotate(node):
    # interchange value
    v1 = node.val
    node.val = node.right.val
    node.right.val = v1
    
    # get right node (with interchanged value, target is to make it left child of root)
    old_right_child = node.right
    
    # set root's right child to root's right child's right child
    node.right = node.right.right

    # interchange root's old right child children (why we don't need right child, it's now the right child of root [line-56])
    old_right_child.right = old_right_child.left

    old_right_child.left = node.left
    node.left = old_right_child

    # Height Recal
    node.left.ht = max(getHeight(node.left.left),getHeight(node.left.right))
    node.ht = max(getHeight(node.left),getHeight(node.right))

def insert(root,val):
    if root != None:
        if root.val > val:
            root.left = insert(root.left,val)
            if balanceFactor(root.left,root.right) > 1:
                # right rotation
                rightRotate(root)
            else:
                root.ht = max(root.ht,root.left.ht + 1)

        elif root.val < val:
            root.right = insert(root.right,val)
            if balanceFactor(root.left,root.right) > 1:
                # left rotation
                leftRotate(root)
            else:
                root.ht = max(root.ht,root.right.ht + 1)
    else:
        root = BST(val)
    return root

def printBST(root):
    if root != None:
        print(f'root:{root.val} ht:{root.ht}',end=" ")
        if root.left != None:
            print(f'left:{root.left.val} ht:{root.left.ht}',end=" ")

        if root.right != None:
            print(f'right:{root.right.val} ht:{root.right.ht}',end=" ")

        print()
        printBST(root.left)
        printBST(root.right)
    
n = int(input())
t = n
root = None
while t > 0:
    t-=1
    e = int(input())
    root = insert(root,e)

printBST(root)