#Is Balanced Tree
from collections import deque
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BST:
    def __init__(self,key):
        self.root=Node(key)
    def insert(self,root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root
    def add(self,key):
        self.insert(self.root,key)
    def height(self,root):
        if not root:
            return 0
        l = self.height(root.left)
        if l == -1:
            return -1
        r = self.height(root.right)
        if r == -1: 
            return -1
        if abs(l-r)>1:
            return -1
        return max(l,r)+1
    def isBalanced(self, root):
        if self.height(root) == -1:
            return False
        return True

for _ in range(int(input())):
    t=int(input())
    l=list(map(int,input().split()))
    bst=BST(l[0])
    for i in range(1,t):
        bst.add(l[i])
    print("Yes" if bst.isBalanced(bst.root) else "No")
