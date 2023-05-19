class MinStack:

    '''I tried using a common pattern in Java where you use Integer.MAX_VALUE to keep track of the min. 
    But python does not have that since int is unbounded.'''

    def __init__(self):
        self.stack = []
        self.minVal
        

    def push(self, val: int) -> None:
        if not self.minVal or val < self.minVal:
            self.minVal = val 
        self.stack.append(val) 
        

    def pop(self) -> None:
        self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal
    
class MinStack2:
    '''Solution I found that uses another stack to keep track of the min seen so far.'''
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
