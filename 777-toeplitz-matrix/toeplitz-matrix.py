class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])


        for i in range(row):
            for j in range(col):

                compare = matrix[i][j]
                k = i
                l = j
                while k+1 < row and l+1 < col:
                
                    if matrix[k+1][l+1] != compare:
                        return False

                    k += 1
                    l += 1

                


        return True
                
