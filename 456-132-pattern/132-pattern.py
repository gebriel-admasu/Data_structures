class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third_value = float('-inf')
        for num in reversed(nums):
            if num < third_value:
                return True

            while stack and stack[-1] < num:
                third_value = stack.pop()

            stack.append(num)
            
        return False
