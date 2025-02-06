class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n + 1))
        current_index = 0
        
        while len(players) > 1:

            current_index = (current_index + k - 1) % len(players)
            
            players.pop(current_index)
        
        return players[0]