class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        original_color = image[sr][sc]
        if original_color == color:
            return image

        def dfs(r,c):

            if not (0 <= r < row and 0 <= c < col and image[r][c] == original_color):
                return
            if image[r][c] ==original_color:
                image[r][c] = color
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0 <= nr < row and 0 <= nc < col:
                    dfs(nr,nc)


        dfs(sr,sc)
        return image