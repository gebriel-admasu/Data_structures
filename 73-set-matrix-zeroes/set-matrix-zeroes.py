class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])


        new_matrix = [["a"] * col for _ in range(row)]

 
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    
                    # updating the col
                    k = 0
                    while k < col:
                   
                        new_matrix[i][k] = 0
                        k += 1

                    # updating the row
                    q = 0
                    while q < row:
                        new_matrix[q][j] = 0
                        q += 1

  
        for i in range(row):
            for j in range(col):
            
                if new_matrix[i][j] == 0:
                    matrix[i][j] = new_matrix[i][j]

        


        print(matrix)