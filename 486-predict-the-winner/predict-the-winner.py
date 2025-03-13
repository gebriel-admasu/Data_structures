from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(start, end):
            if start == end:
                return nums[start]
            pick_start = nums[start] - helper(start + 1, end)
            pick_end = nums[end] - helper(start, end - 1)
            return max(pick_start, pick_end)

        return helper(0, len(nums) - 1) >= 0
