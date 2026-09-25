class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_bucket={}
        
        for i in range(len(nums)):
            
            if nums[i] not in num_bucket:
                
                num_bucket[nums[i]]=1
            else:
                num_bucket[nums[i]]+=1
        
        buckets=[]
        
        for i in range(len(nums)+1):
            buckets.append([])
        
        for key,value in num_bucket.items():
            buckets[value].append(key)
        result=[]
        for key in range((len(buckets)-1),0,-1):
            for num in buckets[key]:
                result.append(num)
            if len(result)==k:
                return result
       
            
            


            
        
        
            
        