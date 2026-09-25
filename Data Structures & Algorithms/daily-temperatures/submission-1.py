class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result=[0]*len(temperatures)

        stack=[]  #pair : [temp,index]

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackInd = stack.pop() 
                result[stackInd]= (i-stackInd)
            stack.append([t,i])
        return result 

        # so basically yaha humne pehle zeros daal diye result array mein ab,humne ek stack bhi le lia ,hum jaise jaise tempreature milega stack mein daal denge and logic ye hai har naya tempreatur echeck hoga stack ke top se if chota stack mein aayega if bada ,matlab bada mil gya check karnge aur jis jis se bada hoga stack se usko nikalte jayenge aur result mein iss abde se unn sab ka jo nikal gaye unka diffrence in days daalte jayenge as per the question                                                                 
        
       
                

            
           


            

        