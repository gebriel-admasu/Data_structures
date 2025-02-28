from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:


        index = nums.index(k)
        prefix_sum = 0
        left_count = defaultdict(int)
        left_count[0] = 1  

        for i in range(index - 1, -1, -1):
            prefix_sum += 1 if nums[i] > k else -1
            left_count[prefix_sum] += 1

        result = 0
        prefix_sum = 0  

        for i in range(index, len(nums)):
            if nums[i] > k:
                prefix_sum += 1
            elif nums[i] < k:
                prefix_sum -= 1

            result += left_count[-prefix_sum] + left_count[-prefix_sum + 1]

        return result
