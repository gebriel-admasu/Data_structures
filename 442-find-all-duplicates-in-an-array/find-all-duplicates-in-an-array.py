class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = Counter(nums)
        output = []
        for i in res:
            if res[i] == 2:
                output.append(i)

        return output