class Solution:
    def isPalindrome(self, s: str) -> bool:
        rs=""   #reverse string
        cs=""   #clean string
        for i in s:
            if i.isalnum():
                cs+=i.lower()
        for i in range((len(cs)-1),-1,-1):
            rs+=cs[i]
        if rs==cs:
            return True
        return False
        