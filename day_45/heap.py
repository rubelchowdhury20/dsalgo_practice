class MaxHeap:
    def __init__(self, array):
        self.array = array
        print(self.array)
        self.buildMaxHeap(self.array)
        print(self.array)
        self.heapSort(self.array, self.heap_size)
        print(self.array)

        

    def parent(self, i):
        return (i-1) >> 1

    def left(self, i):
        return (i << 1) + 1
    
    def right(self, i):
        return (i << 1) + 2


    def maxHeapify(self, array, i, heap_size):
        l = self.left(i)
        r = self.right(i)
        if l < heap_size and array[l] > array[i]:
            largest = l
        else:
            largest = i
        if r < heap_size and array[r] > array[largest]:
            largest = r
        if largest != i:
            flag = array[largest] 
            array[largest] = array[i]
            array[i] = flag
            self.maxHeapify(array, largest, heap_size)


    def buildMaxHeap(self, array):
        self.heap_size = len(array)
        for i in range(self.parent(self.heap_size), -1, -1):
            self.maxHeapify(array, i, self.heap_size)

    def heapSort(self, array, heap_size):
        for i in range(len(array)-1, 0, -1):
            flag = array[0]
            array[0] = array[heap_size-1]
            array[heap_size-1] = flag
            heap_size = heap_size - 1
            self.maxHeapify(array, 0, heap_size)


import random
array = [random.randint(0, 10) for i in range(10)]
# array = [4, 2, 0, 4, 3, 1, 4, 0, 9, 10]
max_heap_obj = MaxHeap(array)