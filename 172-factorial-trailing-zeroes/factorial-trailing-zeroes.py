class Solution:
    def trailingZeroes(self, n: int) -> int:

        def factorial(n):
            if n < 2:
                return 1
        
            return n * factorial(n-1)
        
        ans = factorial(n)
        count_zero = 0
        while ans % 10 == 0:

            count_zero +=1
            ans = ans//10
        
        return count_zero