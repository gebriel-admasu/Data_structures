class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiago = set() 
        negDiago = set()
        res = []
        board = [["."] *n for i in range(n)]
        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or (r+c) in posDiago or (r-c) in negDiago:
                    continue
                col.add(c)
                posDiago.add(r+c)
                negDiago.add(r-c)
                board[r][c] = "Q"

                backtracking(r+1)

                col.remove(c)
                posDiago.remove(r+c) 
                negDiago.remove(r-c)
                board[r][c] = "."
        backtracking(0)
        return res
