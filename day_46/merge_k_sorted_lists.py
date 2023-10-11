###############
# Leetcode 23 #
###############

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        count_dict = {}
        heap = []
        for i in lists:
            current_node = i
            while(current_node is not None):
                val = current_node.val
                if val not in count_dict:
                    count_dict[val] = 1
                    self.insert(heap, val)
                else:
                    count_dict[val] += 1
                current_node = current_node.next
        sorted_heap = self.heapsort(heap)
        root = None
        current_node = root
        for i in sorted_heap:
            for j in range(count_dict[i]):
                if current_node is None:
                    current_node = ListNode(i)
                    root = current_node
                else:
                    current_node.next = ListNode(i)
                    current_node = current_node.next
        return root




    def parent(self, i):
        return (i-1) >> 1
    def left(self, i):
        return (i << 1) + 1
    def right(self, i):
        return (i << 1) + 2

    def insert(self, array, val):
        array.append(val)
        index = len(array)-1
        while(index > 0 and array[index] > array[self.parent(index)]):
            flag = array[self.parent(index)]
            array[self.parent(index)] = array[index]
            array[index] = flag
            index = self.parent(index)

    def maxHeapify(self, array, index, heap_size):
        l = self.left(index)
        r = self.right(index)
        if (l < heap_size and array[l] > array[index]):
            largest = l
        else:
            largest = index
        if (r < heap_size and array[r] > array[largest]):
            largest = r
            
        if largest != index:
            flag = array[largest]
            array[largest] = array[index]
            array[index] = flag
            self.maxHeapify(array, largest, heap_size)



    def heapsort(self, array):
        heap_size = len(array)
        for i in range(heap_size):
            flag = array[heap_size-1]
            array[heap_size-1] = array[0]
            array[0] = flag
            heap_size = heap_size - 1
            self.maxHeapify(array, 0, heap_size)
        return array


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         current_node = None
#         root = None
#         flag = True
#         while(flag):
#             min_ = None
#             min_idx = None
#             for idx, i in enumerate(lists):
#                 if i is not None:
#                     if min_ is not None:
#                         if i.val < min_.val:
#                             min_ = i
#                             min_idx = idx
#                     else:
#                         min_ = i
#                         min_idx = idx
#             if min_ is not None:
#                 if lists[min_idx].next is not None:
#                     lists[min_idx] = lists[min_idx].next
#                 else:
#                     del lists[min_idx]
#                 min_.next = None
#                 if current_node is not None:
#                     current_node.next = min_
#                     current_node = current_node.next
#                 else:
#                     root = min_
#                     current_node = min_
#             else:
#                 flag = False
#         return root



                    
            

        