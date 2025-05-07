class UnionFind:
    def __init__(self, size):
        self.p = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        
    def find(self, x):
        while x != self.p[x]:
            self.p[x] = self.p[self.p[x]]  
            x = self.p[x]
        return x
		
    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x != r_y:
            if self.rank[r_x] > self.rank[r_y]:
                self.p[r_y] = r_x
            elif self.rank[r_x] < self.rank[r_y]:
                self.p[r_x] = r_y
            else:
                self.p[r_y] = r_x
                self.rank[r_x] += 1
 
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        res = []
        for i in range(n):
            for j in range(i+1,n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                res.append((cost,i,j))
        res.sort()
        total = 0
        for cost,u,v in res:
            if not uf.connected(u,v):
                uf.union(u,v)
                total += cost
        return total
