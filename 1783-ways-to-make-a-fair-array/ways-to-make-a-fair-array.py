class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_prefix, odd_prefix = 0, 0
        even_suffix, odd_suffix = sum(nums[::2]), sum(nums[1::2])
        
        count = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_suffix -= num
            else:
                odd_suffix -= num
            
            if even_prefix + odd_suffix == odd_prefix + even_suffix:
                count += 1
            
            if i % 2 == 0:
                even_prefix += num
            else:
                odd_prefix += num
                
        return count
