################
# Leetcode 232 #
################

class MyQueue:

    def __init__(self):
        self.stack = []
        self.dummy_stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        n = len(self.stack)
        for i in range(n-1):
            x = self.stack.pop()
            self.dummy_stack.append(x)
        val = self.stack.pop()
        m = len(self.dummy_stack)
        for i in range(m):
            x = self.dummy_stack.pop()
            self.stack.append(x)
        return val
        

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()