class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        citation_num = len(citations)
        while left < right:
            mid = (left+right+1)//2
            diff = citation_num - mid

            if citations[diff] >= mid:  
                left = mid
            else:
                right = mid -1 

        return left