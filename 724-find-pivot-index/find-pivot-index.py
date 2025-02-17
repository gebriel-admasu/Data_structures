class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix = [0] * len(nums)
        right_prefix = [0] * len(nums)
        for i in range(len(nums)):
            left_prefix[i] = nums[i] + (left_prefix[i - 1] if i > 0 else 0)
        for i in range(len(nums)):
            right_prefix[-i - 1] = nums[-i - 1] + (right_prefix[-i] if i > 0 else 0) 
        for i in range(len(nums)):
            if left_prefix[i] == right_prefix[i]:
                return i
        return -1