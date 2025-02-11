class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1], nums[j]

        for i in range(len(nums)):
            min_index = i
            for j in range(i+1,len(nums)):
                if nums[min_index] > nums[j]:

                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]

