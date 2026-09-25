class Solution:
    def isValid(self, s: str) -> bool:
        my_stack=[]
        for i in range(len(s)):
            if s[i] in ["(","[","{"]:
                my_stack.append(s[i])
            
            
                
            else:
                if not my_stack:   #if my stack is empty return false
                    return False

                if s[i] == ")" and my_stack[-1] == "(":
                    my_stack.pop(-1)
                elif s[i] == "]" and my_stack[-1] == "[":
                    my_stack.pop(-1)
                elif s[i] == "}" and my_stack[-1] == "{":
                    my_stack.pop(-1)
                else:
                    return False
                
        return (len(my_stack)==0)
                    

        


         
                   
        
        