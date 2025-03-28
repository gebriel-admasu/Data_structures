class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        left = min(nums)
        right = max(nums)
    
        def can_rob(mid):
            count = 0
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] <= mid:
                    count += 1
                    i += 2  
                else:
                    i += 1
                if count >= k:
                    return True
            return count >= k
        
        answer = right
        while left <= right:
            mid = (left + right) // 2
            if can_rob(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer