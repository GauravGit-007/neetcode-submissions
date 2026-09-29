class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low=0
        high=len(nums)-1
        

        while low <= high:
            

            mid=(low+high)//2
            value=nums[mid]   # added this so comparison happens with value instead of quering nums each time for comparison

            if  value  < target:
                low=mid + 1

            elif value > target:
                high=mid - 1

            elif value==target:
                return mid
        return -1

                
            
    
        