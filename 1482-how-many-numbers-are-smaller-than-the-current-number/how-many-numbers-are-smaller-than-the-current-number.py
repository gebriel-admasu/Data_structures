class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if num > nums[i]:
                    count +=1
            res.append(count)
        return res