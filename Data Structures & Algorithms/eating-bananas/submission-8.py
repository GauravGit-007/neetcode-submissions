class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low=1
        high=max(piles)
        minRate=high  # currently this is the rate that will help us,eat all the bananas at given time,we could have alos taken a very large number just to fill the space,since its not the anser yet,or any number like a million,just chill its not complex
        
        while low <= high:
            k=(low+high)//2
            totaltime=0


            for i in range(len(piles)):
                totaltime  += math.ceil(piles[i]/k)
 
            if totaltime<=h:
                high=k-1
                minRate=min(minRate,k)
            elif totaltime>=h:
                low=k+1
            
            
        return minRate


        