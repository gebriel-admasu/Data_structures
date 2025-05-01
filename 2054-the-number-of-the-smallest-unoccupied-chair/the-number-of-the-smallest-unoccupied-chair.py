import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        index = [i for i in range(len(times))]
        index.sort(key=lambda i : times[i][0])
        ocupaid_chair = []
        available_chair = [i for i in range(len(times))]
        heapq.heapify(available_chair)  

        for i in index:
            a, l = times[i]
            while ocupaid_chair and ocupaid_chair[0][0] <= a:
                leave_time, chair = heapq.heappop(ocupaid_chair)
                heapq.heappush(available_chair, chair)

            chair = heapq.heappop(available_chair)
            heapq.heappush(ocupaid_chair, (l, chair))

            if i == targetFriend:
                return chair