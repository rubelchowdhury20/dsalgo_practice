

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyQueue:

    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        

    def push(self, x: int) -> None:
        if self.head.val is None:
            self.head.val = x
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        

    def pop(self) -> int:
        if self.head.val is not None:
            val = self.head.val
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = Node(None)
            return val
        else:
            raise Exception("The queue is empty!")
        

    def peek(self) -> int:
        if self.head.val is not None:
            return self.head.val
        else:
            raise Exception("The queue is empty!")
        

    def empty(self) -> bool:
        if self.head.val is None:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()