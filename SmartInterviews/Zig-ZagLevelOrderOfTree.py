#Zig-Zag Level Order of Tree

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
    def levelOrder(self,root):
        #Write your code here
        q=deque()
        q.append(root)
        res=[]
        while q:
            level=[]
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if level:
                res.append(level)
        return res

for _ in range(int(input())):
    t=int(input())
    l=list(map(int,input().split()))
    bst=BST(l[0])
    for i in range(1,t):
        bst.add(l[i])
    res=bst.levelOrder(bst.root)
    for i in range(len(res)):
        if i%2==0:
            print(*res[i][::-1],end=" ")
            continue
        print(*res[i],end=" ")
    print()
