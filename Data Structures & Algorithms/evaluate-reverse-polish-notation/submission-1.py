class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack=[]
        
    
        for i in tokens:
            if i not in "+-*/":
                my_stack.append(int(i))
            else:
                if len(my_stack)>1:
                    
                    b=my_stack.pop()
                    a=my_stack.pop()
                    if i == "+":
                        my_stack.append(a+b)
                    elif i == "-":
                        my_stack.append(a-b)
                    elif i == "*":
                        my_stack.append(a*b)
                    elif i == "/":
                        my_stack.append(int(a/b))
        return my_stack[-1]
        
                    

        
                    



        