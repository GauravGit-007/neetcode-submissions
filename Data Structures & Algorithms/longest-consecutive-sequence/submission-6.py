class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=sorted(nums)
        
        conh=[]        #conh=consecutive count history
        count=1
        if len(nums)!=0:
            

            for i in range(1,len(s)):

                if s[i-1]+1==s[i]:
                    count+=1
                elif s[i-1]==s[i]:
                    continue

                else:
                    conh.append(count)
                    count=1
            conh.append(count)
            output=max(conh)
            return output
        else:
            output=0
            return output
                
        