class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        return [key for key, value in count.items() if value > n / 3]
            
