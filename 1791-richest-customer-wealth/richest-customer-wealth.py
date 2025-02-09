class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        wealth_sum =0
        for num in accounts: 
            wealth_sum = 0
            for j in range(len(num)):
                wealth_sum += num[j]
            max_wealth= max(max_wealth,wealth_sum)
        return max_wealth
