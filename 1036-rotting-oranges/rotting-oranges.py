from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        ans,fresh = 0,0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh +=1
            
                if grid[r][c] == 2:
                    queue.append([r,c])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while queue and fresh >0:
            for i in range (len(queue)):

                r,c = queue.popleft()

            
                for rh,ch in directions:
                    new_r,new_c = r+rh,c+ch
                    if (new_r <0 or new_r == n or new_c <0 or new_c==m or grid[new_r][new_c] !=1):
                        continue
                    grid[new_r][new_c] = 2
                    queue.append([new_r,new_c])
                    fresh -=1
            ans +=1

        return ans if fresh == 0 else -1
            
