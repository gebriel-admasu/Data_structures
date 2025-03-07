class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        next_greater_mapping = {}
      
        stack = []
        for nums in nums2:
            
            while stack and stack[-1] < nums:
                next_greater_mapping[stack.pop()] = nums
          
            stack.append(nums)


      
        return [next_greater_mapping.get(num, -1) for num in nums1]
