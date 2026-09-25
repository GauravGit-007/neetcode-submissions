class Solution:
    def isPalindrome(self, s: str) -> bool:
        rs=''.join(rs.lower() for rs in s if rs.isalnum())
        return rs==rs[::-1]
        
        