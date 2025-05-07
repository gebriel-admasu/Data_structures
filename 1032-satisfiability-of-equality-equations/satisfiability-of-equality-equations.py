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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for equation in equations:
            if equation[1] == '=':
                var1 = ord(equation[0]) - ord('a')
                var2 = ord(equation[3]) - ord('a')
                uf.union(var1, var2)

        
        for equation in equations:
            if equation[1] == '!':
                var1 = ord(equation[0]) - ord('a')
                var2 = ord(equation[3]) - ord('a')
                if uf.connected(var1, var2):
                    return False

        return True