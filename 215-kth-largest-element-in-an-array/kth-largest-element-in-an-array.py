class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap,-num)

        while k > 1:
            val = -heappop(heap)
            k -=1
        return -heap[0]
        # def heapify_down(heap, n, current_idx):
        #     small_child_idx = current_idx
        #     left_idx = 2 * current_idx + 1
        #     right_idx = 2 * current_idx + 2
        #     if left_idx < n and heap[left_idx] < heap[small_child_idx]:
        #         small_child_idx = left_idx
        #     if right_idx < n and heap[right_idx] < heap[small_child_idx]:
        #         small_child_idx = right_idx
        #     if small_child_idx != current_idx:
        #         swap(heap, current_idx, small_child_idx)
        #         heapify_down(heap, n, small_child_idx)
