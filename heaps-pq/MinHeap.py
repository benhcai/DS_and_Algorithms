class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def pop(self):
        if len(self.heap) > 1:
            self.heap[0] = self.heap[-1]
            min = self.heap.pop()
            self.__heapify(0)
            return min
        elif len(self.heap) == 1:
            return self.heap.pop()

    def build(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__heapify(i)
    
    def __percolateUp(self, index):
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.heap[parent] > self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.__percolateUp(parent)

    def __heapify(self, index):
        left = 2*index + 1
        right = 2*index + 2
        smallest = index
        if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
            smallest = left
        if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[smallest]
            self.heap[smallest] = temp
            self.__heapify(smallest)

    def verify(self):
        for i in range(len(self.heap)-2):
            left = 2*i + 1
            right = 2*i + 2
            if self.heap[i] > self.heap[left] or self.heap[i] > self.heap[right]:
                return False
            return True

    def display(self):
        cols = 1
        i = 0
        all = []
        while i < len(self.heap):
            arr = []
            curr = []
            while i < cols:
                if len(curr) == 2:
                    arr.append(curr)
                    curr = []
                curr.append(self.heap[i])
                i += 1
            if curr:
                arr.append(curr)
                curr = []
            all.append(arr)
            cols = cols*2 + 1

        spaces = 20
        for row in range(len(all)):
            print(' ' * spaces, all[row])
            spaces = spaces - int(2*row) - 3

heap = MinHeap()

import random
for _ in range(15):
    rand = random.randint(0,30)
    heap.insert(rand)
print(heap.heap)
print(heap.verify())
heap.display()
