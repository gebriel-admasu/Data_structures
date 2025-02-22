class Solution:
    def numberOfWays(self, s: str) -> int:
        count_zero = s.count("0")
        count_one = len(s) - count_zero
        ans = 0
        c0 = 0
        c1 = 0

        for num in s:
            if num == "0":
                ans += c1 *(count_one - c1)
                c0 +=1
           
            else:
                ans += c0 *(count_zero - c0)
                c1 += 1
        return ans
               
        
