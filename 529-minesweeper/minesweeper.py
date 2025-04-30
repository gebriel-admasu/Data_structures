class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row = len(board)
        col = len(board[0])
        r,c = click
        if board[r][c] == "M":
            board[r][c] = "X"
        directions = [(1,1),(1,0),(-1,0),(0,-1),(-1,-1),(0,1),(-1,1),(1,-1)]
        def dfs(r,c):
            if board[r][c] !="E":
                return
            count= 0
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0 <= nr < row and 0 <= nc < col:

                    if board[nr][nc] == "M":
                        count +=1
            if count > 0:

                board[r][c] = str(count)
                return 
            board[r][c] = "B"
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0 <= nr < row and 0 <= nc < col:
                    dfs(nr,nc)

        dfs(r,c)
        return board






    