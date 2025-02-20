from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location_deltas = [0] * 1001
      
        for passengers, start_location, end_location in trips:
            
            location_deltas[start_location] += passengers

            location_deltas[end_location] -= passengers
      
    
        return all(current_passengers <= capacity for current_passengers in accumulate(location_deltas))