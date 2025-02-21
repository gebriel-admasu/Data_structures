class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        zero_count = 0  
        
        for char in s:
            if char == '0':
                count += zero_count 
            else:
                zero_count += 1  
        
        return count
