class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0 
        x, y = 0, 0  
        max_distance = 0

        obstacle_set = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2:  
                direction_index = (direction_index - 1) % 4
            elif cmd == -1: 
                direction_index = (direction_index + 1) % 4
            else: 
                dx, dy = direction_vectors[direction_index]
                for _ in range(cmd):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_distance = max(max_distance, x**2 + y**2)
                    else:
                        break

        return max_distance