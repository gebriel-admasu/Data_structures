class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count("1")
        res = 0
        zeros = 0

        for i in range(len(s)-1):
            if s[i] =="0":
                zeros +=1
            else:
                one -=1
            res = max(res,one + zeros)
        return res
        #     left = s[:i]
        #     right = s[i:]
        #     ones = 0
        #     zeros =0 
        #     for num in left:
        #         if num == 0:

        #             zeros += 1
        #         else:
        #             ones +=1
        #         total = zeros + ones
        #     res = max(res,total)
        # return res