class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            correct_pos = nums[i] - 1
            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        missing_numbers = []
        for i in range(n):
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
        
        return missing_numbers