################
# Leetcode 347 #
################

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_elements = []
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        for i in freq_dict:
            heap.append([i, freq_dict[i]])
        heap_size = self.buildMaxHeap(heap)
        for i in range(k):
            maximum, heap_size = self.extractMaximum(heap, heap_size)
            freq_elements.append(maximum[0])
        return freq_elements


    def parent(self, index):
        return (index - 1) >> 1

    def left(self, index):
        return (index << 1) + 1

    def right(self, index):
        return (index << 1) + 2

    def maxHeapify(self, array, index, heap_size):
        l = self.left(index)
        r = self.right(index)
        if l < heap_size and array[l][1] > array[index][1]:
            largest = l
        else:
            largest = index
        if r < heap_size and array[r][1] > array[largest][1]:
            largest = r
        if largest != index:
            flag = array[largest]
            array[largest] = array[index]
            array[index] = flag
            self.maxHeapify(array, largest, heap_size)

    def extractMaximum(self, array, heap_size):
        maximum = array[0]
        array[0] = array[heap_size-1]
        heap_size = heap_size - 1
        self.maxHeapify(array, 0, heap_size)
        return maximum, heap_size

    def buildMaxHeap(self, array):
        heap_size = len(array)
        for i in range(self.parent(heap_size-1), -1, -1):
            self.maxHeapify(array, i, heap_size)
        return heap_size

        