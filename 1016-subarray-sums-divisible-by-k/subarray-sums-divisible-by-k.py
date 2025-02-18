class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = {0: 1}
        current_sum = 0
        
        for num in nums:
            current_sum += num
            reminder = current_sum % k
            if reminder < 0:
                reminder += k
            
            res += prefix.get(reminder, 0)
            prefix[reminder] = prefix.get(reminder, 0) + 1

        return res
