class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        zero_count = 0  # Tracks number of '0's seen
        
        for char in s:
            if char == '0':
                count += zero_count  # Each zero contributes swaps
            else:
                zero_count += 1  # Counting '1's encountered
        
        return count
