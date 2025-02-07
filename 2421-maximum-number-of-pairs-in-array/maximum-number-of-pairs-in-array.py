class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        num_counter = Counter(nums)
    
        pair  = sum(count // 2 for count in num_counter.values())
        n = pair*2

        return [pair , len(nums)-n]

      
    
