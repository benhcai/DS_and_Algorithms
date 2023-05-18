class MaxHeap:
    def __init__(self):
        self.heap = []
    
    # O(logn)
    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    # O(1)
    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    # O(logn)
    def removeMax(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    # O(logn)
    def __percolateUp(self, index):
        parent = (index-1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.__percolateUp(parent)

    # O(logn)
    def __maxHeapify(self, index):
        left = index*2 + 1
        right = index*2 + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            temp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = temp
            self.__maxHeapify(largest)
    
    # O(n)
    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__maxHeapify(i)

heap = MaxHeap()
heap.insert(5)
heap.insert(4)
heap.insert(2)
heap.insert(3)
heap.insert(1)
heap.insert(1)
heap.removeMax()

arr = [1,5,2,12,5,34,1,5,61,2,33,13]
heap.buildHeap(arr)
print(heap.heap)
print(heap.getMax())
