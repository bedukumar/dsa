"""
Heap Tree : is a complete binary tree,that comes with the Heap Order Property [Max heap,Min heap]


"""

class MaxHeapTree:
    def __init__(self):
        self.heap=[0]*100
        self.size=1
    def insert(self,val):
        self.size += 1
        index = self.size
        self.heap[index] = val 
        while index > 1:
            if self.heap[index//2]<self.heap[index]:
                self.heap[index],self.heap[index//2] = self.heap[index//2],self.heap[index]
                index = index//2
            else:
                return
    def show(self):
        print(*self.heap[1:self.size],sep=" ")

ht = MaxHeapTree()
ht.insert(50)
ht.insert(55)
ht.insert(53)
ht.insert(52)
ht.insert(54)
ht.show()