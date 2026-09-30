class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        minRate=float('inf')
        piles=sorted(piles)
        low=1
        high=max(piles)
        
        while low <= high:
            k=(low+high)//2
        

        
            totaltime=0


            for i in range(len(piles)):
                totaltime+=self.taim(piles[i],k)
            if totaltime<=h:
                high=k-1
                minRate=min(minRate,k)
            elif totaltime>=h:
                low=k+1
            
            
        return minRate
        


    
    def taim(self, num: int, rate: int) -> int:
        if num%rate != 0:
            res=(num//rate) + 1
        else:
            res=num//rate
        return res



        