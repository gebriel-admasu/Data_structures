class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            x_r = find(x)
            y_r = find(y)

            if x_r != y_r:
                if rank[x_r] > rank[y_r]:
                    p[y_r] = x_r
                elif rank[x_r] < rank[y_r]:
                    p[x_r] = y_r
                else:
                    p[y_r] = x_r
                    rank[x_r] += 1
                return True

            return False
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []
