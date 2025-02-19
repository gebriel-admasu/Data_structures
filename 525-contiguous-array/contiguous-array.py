class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_o = 0
        count_l = 0
        res = 0
        prefix = {}

        for i in range (len(nums)):
                if nums[i] == 0:
                    count_o  +=1
                else:
                    count_l +=1
                diff = count_l - count_o
                if diff not in prefix:

                    prefix[diff] = i


                if count_o == count_l:

                    res = count_o + count_l
                else:
                    idx = prefix[diff]
                    res = max(res,i-idx)

        return res