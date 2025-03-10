class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        if target == 1:
            return 0
        while maxDoubles:
            r = target % 2
            target = target // 2
            ans += (r + 1)
            maxDoubles -= 1

            if target == 1:
                break
        
        return target + ans - 1