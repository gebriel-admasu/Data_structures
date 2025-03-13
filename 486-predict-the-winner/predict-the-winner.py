class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recurse(start, end):
            if start == end:
                return nums[start]
            pick_start = nums[start] - recurse(start + 1, end)
            pick_end = nums[end] - recurse(start, end - 1)
            return max(pick_start, pick_end)
        res = recurse(0, len(nums) - 1)
        if res >=0:

            return  True
        else:
            return False
