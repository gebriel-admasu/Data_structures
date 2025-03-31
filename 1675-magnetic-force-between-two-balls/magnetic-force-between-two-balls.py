class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def good(mid):
            count = 1
            prev = position[0]  
            for i in range(1, len(position)):
                if position[i] - prev >= mid:
                    prev = position[i]  
                    count += 1
                    if count >= m:
                        return True
            return False

        res = 0
        low, high = 1, position[-1] - position[0]

        while low <= high:
            mid = (low + high) // 2
            if good(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res
