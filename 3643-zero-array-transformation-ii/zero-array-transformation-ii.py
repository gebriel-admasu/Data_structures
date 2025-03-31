class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        
        if all(x == 0 for x in nums):
            return 0
        
        low, high = 1, len(queries)
        result = -1

        def can_zero_out(mid: int) -> bool:
            diff = [0] * (n + 1)
            temp_nums = nums[:]
            

            for i in range(mid):
                l, r, val = queries[i]
                diff[l] -= val
                if r + 1 < n:
                    diff[r + 1] += val
            
            current = 0
            for i in range(n):
                current += diff[i]
                temp_nums[i] += current
            
            return all(x <= 0 for x in temp_nums)  

        while low <= high:
            mid = (low + high) // 2
            if can_zero_out(mid):
                result = mid
                high = mid - 1  
            else:
                low = mid + 1  
        
        return result
