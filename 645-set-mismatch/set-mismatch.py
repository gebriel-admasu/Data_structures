class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        nums.sort()
        duplicate = -1
        missing = 1 

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                duplicate = nums[i]
                missing = i+1
                break
           
        expected_sum = (1 + len(nums)) * len(nums) // 2
        actual_sum = sum(nums)
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]