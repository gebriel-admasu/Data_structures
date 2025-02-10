class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix),(len(matrix[0]))
        res = []
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        turn = 0
        visited = set()
        row ,col = 0, 0

        for i in range(rows*cols):

            res.append(matrix[row][col])
            visited.add((row,col))
            new_row,new_col = row + direction[turn][0], col + direction[turn][1]

            if not (0 <= new_row < rows and 0 <= new_col < cols) or ((new_row,new_col)) in visited:
                turn = (turn +1)%4
                row,col = row + direction[turn][0], col + direction[turn][1]

            elif (new_row,new_col) not in visited:
                row = new_row
                col = new_col
            

        return res


            

