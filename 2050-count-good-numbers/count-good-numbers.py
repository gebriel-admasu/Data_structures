class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(x, y, mod):
            res = 1
            while y > 0:
                if y % 2 == 1:
                    res = (res * x) % mod
                x = (x * x) % mod
                y //= 2
            return res
        
        even_positions = (n + 1) // 2 
        odd_positions = n // 2 
        
        return (power(5, even_positions, MOD) * power(4, odd_positions, MOD)) % MOD
