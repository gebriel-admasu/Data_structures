class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.n = n
        for i in range(1,n+1):
            heapq.heappush(self.heap,i)

    def reserve(self) -> int:
        val = heapq.heappop(self.heap)
        return val

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)