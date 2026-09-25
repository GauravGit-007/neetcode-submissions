class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        #count=1
        res=[]
        #k=1

        if len(nums)!=0:
            for i in nums:
                count=1
                k=1
                if (i - 1) not in nums:
                    


                    while (i+k) in nums:
                        count+=1
                        k+=1
                

                    
                    

                res.append(count)
                

            output=max(res)
            return output
        else:
            return 0


                
        