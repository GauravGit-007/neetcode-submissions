class MinStack:

    def __init__(self):
        self.my_stack=[]
        self.mini_stack=[]
        

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        if not self.mini_stack:
                self.mini_stack.append(val)
        else:
                self.mini_stack.append(min(val,self.mini_stack[-1]))
               
                
        

    def pop(self) -> None:
        self.my_stack.pop()
        self.mini_stack.pop()
        

    def top(self) -> int:
        return self.my_stack[-1]
        

    def getMin(self) -> int:
        return self.mini_stack[-1]
        
