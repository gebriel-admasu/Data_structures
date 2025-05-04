import heapq

class MedianFinder:

    def __init__(self):
        self.s_heap = []
        self.l_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s_heap, -num)

        if self.l_heap and -self.s_heap[0] > self.l_heap[0]:
            val = -heapq.heappop(self.s_heap)
            heapq.heappush(self.l_heap, val)

        if len(self.s_heap) > len(self.l_heap) + 1:
            val = -heapq.heappop(self.s_heap)
            heapq.heappush(self.l_heap, val)
        elif len(self.l_heap) > len(self.s_heap):
            val = heapq.heappop(self.l_heap)
            heapq.heappush(self.s_heap, -val)

    def findMedian(self) -> float:
        if len(self.s_heap) == len(self.l_heap):
            return (-self.s_heap[0] + self.l_heap[0]) / 2
        else:
            return -self.s_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()