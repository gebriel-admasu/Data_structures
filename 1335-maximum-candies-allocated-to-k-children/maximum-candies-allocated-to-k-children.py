from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0

        def good(mid):
            count = 0
            for i in range(len(candies)):
                if candies[i] >= mid:
                    count += candies[i] // mid
                if count >= k:
                    return True
            return False

        low = 1
        high = total // k
        res = 0
        while low <= high:
            mid = (low + high) // 2

            if good(mid):
                low = mid + 1
                res = mid
            else:
                high = mid - 1

        return res
                    