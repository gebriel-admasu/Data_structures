from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_zero = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1  # Count number of zeros in the window
            
            # Shrink window if zero count exceeds k
            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1  # Decrement zero count if leftmost element is zero
                left += 1  # Move left pointer

            # Update max_length after adjusting the window
            max_length = max(max_length, right - left + 1)

        return max_length
