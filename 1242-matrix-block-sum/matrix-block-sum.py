class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        from itertools import product

        m, n = len(mat), len(mat[0])
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i, j in product(range(m), range(n)):
            prefix[i+1][j+1] = mat[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
        
        result = [[0] * n for _ in range(m)]
        
        for i, j in product(range(m), range(n)):
            r1, c1 = max(0, i-k), max(0, j-k)
            r2, c2 = min(m-1, i+k), min(n-1, j+k)
            
            result[i][j] = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
        
        return result
