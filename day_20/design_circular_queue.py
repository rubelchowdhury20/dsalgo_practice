################
# Leetcode 622 #
################

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = Node()
        self.tail = self.head

        

    def enQueue(self, value: int) -> bool:
        if self.size < self.capacity:
            if self.head.val is None:
                self.head.val = value
                self.size += 1
                if self.size == self.capacity:
                    self.tail.next = self.head
                    self.head.prev = self.tail
                return True
            else:
                self.tail.next = Node(value)
                self.tail.next.prev = self.tail
                self.tail = self.tail.next
                self.size += 1
                if self.size == self.capacity:
                    self.tail.next = self.head
                    self.head.prev = self.tail
                return True

        else:
            return False
        

    def deQueue(self) -> bool:
        if self.head.val is not None:
            if self.size == 1:
                self.head.val = None
            else:
                self.head = self.head.next
                self.head.prev = None
            if self.size == self.capacity:
                self.tail.next = None
                self.head.prev = None
            self.size -= 1
            return True
        

    def Front(self) -> int:
        if self.head.val is not None:
            return self.head.val
        else:
            return -1
        

    def Rear(self) -> int:
        if self.tail.val is not None:
            return self.tail.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.head.val is None:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()