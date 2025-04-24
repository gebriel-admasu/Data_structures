class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def check(radius):
            i = j = 0
            while i < len(houses):
                while j < len(heaters) and abs(heaters[j] - houses[i]) > radius:
                    j += 1
                if j == len(heaters):  
                    return False
                i += 1
            return True
        
        left, right = 0, max(max(houses), max(heaters))
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
