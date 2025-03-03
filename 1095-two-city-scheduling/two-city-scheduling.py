class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda cost: cost[0] - cost[1])  
        half_people = n // 2

        first_half = sum(costs[i][0] for i in range(half_people)) 
        second_half = sum(costs[i][1] for i in range(half_people, n))  
        total = first_half + second_half

        return total
            