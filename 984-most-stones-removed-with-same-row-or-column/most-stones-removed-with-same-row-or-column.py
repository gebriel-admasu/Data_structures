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
            return True
        return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)

        parent = set()
        for i in range(n):
            parent.add(uf.find(i))

        return n - len(parent)