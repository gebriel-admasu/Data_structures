class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [-1] * (n + 1) 
        
        for i in range(1, n + 1):
            if color[i] == -1: 
                queue = deque([i])
                color[i] = 0 
                
                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[current] 
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False 
        return True