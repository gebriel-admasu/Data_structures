from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])

        n = len(rooms)
        visited = [False]* n
        visited[0] = True
        count_visited = 0
        while q:
            node = q.popleft()
            count_visited +=1

            for nig in rooms[node]:
                if not visited[nig]:
                    visited[nig] = True
                    q.append(nig) 
       
        return count_visited == n
  
            
