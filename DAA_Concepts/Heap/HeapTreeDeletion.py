class MaxHeapTree:
    def __init__(self):
        self.heap = [0]*100
        self.size = 0

    def insert(self, val):
        self.size += 1
        index = self.size
        self.heap[index] = val
        while index > 1:
            if self.heap[index//2] < self.heap[index]:
                self.heap[index], self.heap[index //
                                            2] = self.heap[index//2], self.heap[index]
                index = index//2
            else:
                return
    def delete(self):
        if self.size == 0:
            print("Nothing to delete")
            return 
        self.heap[1] = self.heap[self.size]
        self.size-=1
        i=1
        while i<self.size:
            left,right = 2*i, 2*i+1
            if left<self.size and self.heap[i]<self.heap[left]:
                self.heap[i],self.heap[left]=self.heap[left],self.heap[i]
                i=left
            elif left<self.size and self.heap[i]<self.heap[right]:
                self.heap[i],self.heap[right]=self.heap[right],self.heap[i]
                i=right
            else:
                return 
            



    def show(self):
        print(*self.heap[1:self.size+1], sep=" ")


ht = MaxHeapTree()
ht.insert(50)
ht.insert(55)
ht.insert(53)
ht.insert(52)
ht.insert(54)
ht.show()
ht.delete()
ht.show()
