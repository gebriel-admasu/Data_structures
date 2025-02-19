class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix= {0:1}
        res = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            diff = current_sum - goal

            res += prefix.get(diff,0)
            prefix[current_sum] = prefix.get(current_sum,0) +1
        
        return res