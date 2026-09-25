class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_message = ''
        for message in strs:
            encoded_message += str(len(message)) + "#" + message
       
        return encoded_message
        

    def decode(self, s: str) -> List[str]:
        decoded_message=[]
        fetch=''
        i=0
        while i<len(s):
            j=i
            
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            fetch=s[(j+1):(j+1+length)]
            decoded_message.append(fetch)
            i=j+1+length
        return decoded_message



