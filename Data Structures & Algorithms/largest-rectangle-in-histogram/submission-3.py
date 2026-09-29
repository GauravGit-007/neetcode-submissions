class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        maxArea=0
        
        for i,h in enumerate(heights + [0]):
            start=i
            while stk and stk[-1][-1]>h:
                index,height=stk.pop()
                maxArea=max(maxArea, height * (i-index))
                start=index
            stk.append((start,h))
        
        return maxArea
        

        


        