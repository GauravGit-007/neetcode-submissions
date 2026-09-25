class Solution:
    def trap(self, height: List[int]) -> int:
        ttw=0     #total trapped water
        l=0
        r=len(height)-1
        max_left=0
        max_right=0
        while l<r:
            if height[l]<height[r]:
                if height[l]>=max_left:
                    max_left=height[l]
                else:
                    ttw+=max_left-height[l]
                l+=1
            else:
                if height[r]>=max_right:
                    max_right=height[r]
                else:
                    ttw+=max_right-height[r]
                r-=1
        return ttw






        