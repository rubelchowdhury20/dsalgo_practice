import math
import random

class MaxPriorityQueue:
    def __init__(self):
        self.array = []
        self.heap_size = len(self.array)

    def __str__(self):
        return str(self.array[:self.heap_size])

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

    def increaseKey(self, array, i, key):
        if key < array[i]:
            raise Exception("key value is smaller than the existing one")
        else:
            array[i] = key
            current_index = i
            while(current_index>0 and array[current_index]>array[self.parent(current_index)]):
                flag = array[self.parent(current_index)]
                array[self.parent(current_index)] = array[current_index]
                array[current_index] = flag
                current_index = self.parent(current_index)

    def insert(self, key):
        self.heap_size += 1
        self.array.append(-math.inf)
        self.increaseKey(self.array, self.heap_size-1, key)

    def max(self):
        return self.array[0]
    
    def extractMax(self):
        max_ = self.array[0]
        self.array[0] = self.array[self.heap_size-1]
        self.heap_size -= 1
        self.maxHeapify(self.array, 0, self.heap_size)
        return max_
        


mpq = MaxPriorityQueue()
elements = [random.randint(0, 10) for i in range(10)]
print(elements)
for i in elements:
    mpq.insert(i)
print(mpq)
print(mpq.max())
mpq.extractMax()
print(mpq)

    

