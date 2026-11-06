class MinStack:

    def __init__(self):
        self.stack = []
        self.m_stack = []
        self.mini = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini = min(val, self.m_stack[-1] if self.m_stack else val)
        self.m_stack.append(self.mini)
        
    def pop(self) -> None:
        self.stack.pop()
        self.m_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.m_stack[-1]
        
