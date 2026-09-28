class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        true_car_track=[(l,v) for l,v in zip(position,speed)]
        true_car_track=sorted(true_car_track, key=lambda x:x[0], reverse=True)  #this is the line to sort the list ,key is what to sort in this case only the first element of the pairs from the list,in this case positions of the cars from target 
        
        stk=[]     #this stack will store the time of the leaders of the car fleets,the leader is the one who reached ata position first and is slowind down other cars because it has a higher alone them then those behind it and hence a fleet is formed
       

        for l,v in true_car_track:
            alone_time=((target-l)/v)
            if not stk or alone_time>stk[-1]:
                stk.append(alone_time)
        
        return len(stk)


        

        


        