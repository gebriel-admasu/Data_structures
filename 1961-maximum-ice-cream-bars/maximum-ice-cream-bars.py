class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        count = 0
        for num in costs:
            total += num
            if total > coins:
                 break
            count +=1
        return count

       