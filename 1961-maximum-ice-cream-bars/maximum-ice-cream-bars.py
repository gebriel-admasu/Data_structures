class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0
        
        max_value = max(costs)
        count = [0] * (max_value + 1) 

        for num in costs:
            count[num] += 1
        
        total = 0
        ice_creams = 0
        
        for price, frequency in enumerate(count):
            while frequency > 0 and total + price <= coins:
                total += price
                ice_creams += 1
                frequency -= 1
                
        return ice_creams
