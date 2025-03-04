class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        max_height_in_row = [max(row) for row in grid]
      
        max_height_in_column = [max(column) for column in zip(*grid)]
      
      
        total_increase = sum(
            min(max_height_in_row[i], max_height_in_column[j]) - grid[i][j]
            for i in range(len(grid))
            for j in range(len(grid[0]))
        )
      
        return total_increase
