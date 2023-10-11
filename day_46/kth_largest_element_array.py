################
# Leetcode 215 #
################

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        self.buildMinHeap(heap)
        for i in nums[k:]:
            if i > heap[0]:
                heap[0] = i
                self.minHeapify(heap, 0, k)
        return heap[0]

    def parent(self, i):
        return (i-1) >> 1
    def left(self, i):
        return (i << 1) + 1
    def right(self, i):
        return (i << 1) + 2

    def minHeapify(self, array, index, heap_size):
        l = self.left(index)
        r = self.right(index)
        if l < heap_size and array[l] < array[index]:
            smallest = l
        else:
            smallest = index
        if r < heap_size and array[r] < array[smallest]:
            smallest = r
        if smallest != index:
            flag = array[smallest]
            array[smallest] = array[index]
            array[index] = flag
            self.minHeapify(array, smallest, heap_size)

    def buildMinHeap(self, array):
        heap_size = len(array)
        for i in range(self.parent(heap_size-1),-1,-1):
            self.minHeapify(array, i, heap_size)

# alternate solution

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            if i > heap[0]:
                heapq.heapreplace(heap, i)
        return heap[0]


        