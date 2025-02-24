class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        result = [0] * n
        for i in range(n):
            left_sum = nums[i] * i - (prefix[i - 1] if i > 0 else 0)
            right_sum = (prefix[n - 1] - prefix[i]) - nums[i] * (n - i - 1)
            result[i] = left_sum + right_sum

        return result
