class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap = []
    
        for row_index, row in enumerate(grid):
            print(row_index,row)
            for val in row:
                heapq.heappush(max_heap, (-val, row_index))  

        selected_from_row = [0] * len(grid)
        total_sum = 0
        count = 0

        while max_heap and count < k:
            val, row_index = heapq.heappop(max_heap)
            if selected_from_row[row_index] < limits[row_index]:
                total_sum += -val  
                selected_from_row[row_index] += 1
                count += 1

        return total_sum