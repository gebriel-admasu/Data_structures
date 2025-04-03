class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def quicksort(array):
            if len(array) < 2:
                return array

            pilot = array[0]
            less = [i for i in array[1:] if i <= pilot]
            greater = [i for i in array[1:] if i > pilot]
            return quicksort(less) + [pilot] + quicksort(greater)

        nums = quicksort(nums)
        left,right = 0,len(nums)
        while right > left:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return left 


