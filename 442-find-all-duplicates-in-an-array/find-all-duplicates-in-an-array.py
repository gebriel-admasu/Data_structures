class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num,0) +1
        return [key for key, value in res.items() if value == 2]

