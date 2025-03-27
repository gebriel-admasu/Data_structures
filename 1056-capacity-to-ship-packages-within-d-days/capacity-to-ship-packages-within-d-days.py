class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def validate(capacity):
            day_count = 1
            cap_count = 0
            for weight in weights:
                cap_count += weight
                if cap_count > capacity:
                    day_count +=1
                    cap_count = weight
                    if day_count > days:
                        return False

            return True
        
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left+right)//2
            if validate(mid):
                right = mid -1
            else:
                left = mid +1

        return left

