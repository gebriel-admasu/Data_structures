class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = -1
        max_index = 0
        
        for i in range(len(mat)):
            current_count = sum(mat[i])
            if current_count > max_count:
                max_count = current_count
                max_index = i
            elif current_count == max_count and i < max_index:
                max_index = i
        
        return [max_index, max_count]