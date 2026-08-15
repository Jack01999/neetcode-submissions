class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            newMin = min(val, self.minStack[-1])
            self.minStack.append(newMin)
        else:
            self.minStack.append(val)
        
    def pop(self) -> None:
        if len(self.stack) > 0:
            del self.stack[-1]
            del self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
