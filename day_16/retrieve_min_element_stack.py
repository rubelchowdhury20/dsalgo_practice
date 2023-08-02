################
# Leetcode 155 #
################

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min = val
            self.stack.append(val)

        else:
            if val < self.min:
                self.stack.append(2*val - self.min)
                self.min = val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x <= self.min:
            return_value = self.min
            self.min = -(x - 2*self.min)
            return return_value
        else:
            return x

    def top(self) -> int:
        if self.stack[-1] < self.min:
            return self.min
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()