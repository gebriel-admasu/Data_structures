class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i ,n = 1,len(piles)
        max_res = 0
       
        for i in range(n-2,(len(piles) // 3)-1,-2):
            max_res += piles[i]

        return max_res

