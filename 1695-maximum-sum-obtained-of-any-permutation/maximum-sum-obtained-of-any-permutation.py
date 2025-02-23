class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        ind_freq = [0]* (n+1)
        total = 0
        for start,end in requests:
            ind_freq[start] += 1

            ind_freq[end +1] -=1
        for i in range(1,n):
            ind_freq[i] += ind_freq[i-1]
        
        ind_freq.sort(reverse = True)
        nums.sort(reverse = True)

        for i in range(n):
            total += ind_freq[i] * nums[i]

        modulus = 10**9 + 7

        return total % modulus

