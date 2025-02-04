class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n*2
        ans = [0]*m

        for i in range (m):
            index = i % n
            ans[i] = nums[index]
        return ans