class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                low, high = 0, cols - 1
                while low <= high:
                    m = (low + high) // 2
                    if matrix[mid][m] > target:
                        high = m - 1
                    elif matrix[mid][m] < target:
                        low = m + 1
                    else:
                        return True
                return False
        
        return False
