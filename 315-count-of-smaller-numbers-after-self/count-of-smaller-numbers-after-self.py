class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        indexed_nums = list(enumerate(nums))  
        
        def merge_sort(enums):
            if len(enums) <= 1:
                return enums
            mid = len(enums) // 2
            left = merge_sort(enums[:mid])
            right = merge_sort(enums[mid:])
            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or (i < len(left) and left[i][1] <= right[j][1]):
                    merged.append(left[i])
                    result[left[i][0]] += j  
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return merged

        merge_sort(indexed_nums)
        return result