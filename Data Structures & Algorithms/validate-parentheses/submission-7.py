class Solution:
    def isValid(self, s: str) -> bool:
        my_stack=[]
        for i in range(len(s)):
            if len(my_stack)!=0:
            
                if s[i] == ")" and my_stack[-1] == "(":
                    my_stack.pop(-1)
                elif s[i] == "]" and my_stack[-1] == "[":
                    my_stack.pop(-1)
                elif s[i] == "}" and my_stack[-1] == "{":
                    my_stack.pop(-1)
                
                else:
                    my_stack.append(s[i])
            else:
                my_stack.append(s[i])

        if len(my_stack) == 0:
            return True
        else:
            return False


         
                   
        
        