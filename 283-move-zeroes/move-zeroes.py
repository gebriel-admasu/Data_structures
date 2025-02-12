class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for num in nums:
            if num != 0:
                nums[zero_index] = num
                zero_index +=1
        for i in range(zero_index,len(nums)):
            nums[i] = 0
            