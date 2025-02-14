class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float("inf")

        for left in range(len(nums) - 2):
            right = left + 1
            third = len(nums) - 1

            while right < third:
                three_sum = nums[left] + nums[right] + nums[third]
                
                if abs(target - three_sum) < abs(target - closest_sum):
                    closest_sum = three_sum

                if three_sum < target:
                    right += 1
                else:
                    third -= 1

        return closest_sum

 


