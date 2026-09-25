class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack=[]
        result=int()
    
        for i in tokens:
            if i not in "+-*/":
                my_stack.append(int(i))
            else:
                if len(my_stack)>1:
                    #result=int() i intialized it but didnot use
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
        result=my_stack[-1]
        return result
                    

        
                    



        