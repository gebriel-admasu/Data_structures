class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0 
        right = len(s) - 1
        count = 0
        
        while left < right:
            if s[left] != s[right]:
                if count >= 1:  
                    return False
                return (s[left:right] == s[left:right][::-1]) or (s[left+1:right+1] == s[left+1:right+1][::-1])
            left += 1
            right -= 1 
            
        return True
