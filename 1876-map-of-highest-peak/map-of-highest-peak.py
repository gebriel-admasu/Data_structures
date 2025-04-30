from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        height = [[-1]* cols for _ in range(rows)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append((i,j))
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr,nc))
            
        return height
