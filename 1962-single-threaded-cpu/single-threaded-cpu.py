from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed_tasks = sorted([(tasks[i][0], tasks[i][1], i) for i in range(n)])
        available_tasks = []
        result = []
        current_time = 0
        task_index = 0

        while task_index < n or available_tasks:
            while task_index < n and indexed_tasks[task_index][0] <= current_time:
                arrival_time, processing_time, original_index = indexed_tasks[task_index]
                heappush(available_tasks, (processing_time, original_index))
                task_index += 1

            if available_tasks:
                processing_time, original_index = heappop(available_tasks)
                result.append(original_index)
                current_time += processing_time
            elif task_index < n:
                current_time = indexed_tasks[task_index][0]

        return result