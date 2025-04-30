class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        count = 0
        for num in nums:

            heappush(heap,num)
        if len(nums) >= 2:
            while heap[0] < k:
                val1 = heappop(heap)
                val2 = heappop(heap)
                insert_val = (min(val1,val2)*2 + max(val1,val2))

                heappush(heap,insert_val)
                count +=1

        return count
            